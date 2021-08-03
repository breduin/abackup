"""
Making the archive (tar) files.
"""

import os
import tarfile
import asyncio
import sys
from datetime import datetime
from loguru import logger
from config import FILES_TO_ARCHIVE, DB, PREFIX_TAR_DB, PREFIX_TAR_FILES, MAX_ARCHIVES
from time_info import SpbTime
from status import status


def date_time_stamp() -> str:
    """
    Returns string with current date and time for given time zone 
    in format "2021-07-30_17:50"
    """
    today = datetime.now(tz=SpbTime())
    return f"{today.date()}_{today.time().isoformat(timespec='minutes')}"


def get_archive_file_name() -> str:
    """
    Returns name for archive file
    """
    return f"{PREFIX_TAR_FILES}_{date_time_stamp()}.tar"

def get_archive_db_name() -> str:
    """
    Returns name for archive database
    """
    return f"{PREFIX_TAR_DB}_{date_time_stamp()}.tar"


@logger.catch()
def get_tar_files() -> str:
    """
    Adds files from list FILES_TO_ARCHIVE to tar archive.

    UNIX path separator '/' is used to display the file or directory name.
    """
    global status
    archive_name = get_archive_file_name()
    with tarfile.open(archive_name, "w") as tar:
        for name in FILES_TO_ARCHIVE:
            try:
                tar.add(name)
                logger.info(f"File (directory) {name.split('/')[-1]} is added to archive.")
            except FileNotFoundError:
                logger.error(f"File (directory) {name.split('/')[-1]} is not found.")
                this_method_name = sys._getframe().f_code.co_name
                status[this_method_name] = False

    return archive_name


@logger.catch()
def get_db_dump() -> list:
    """
    Get database dump and returns its name (as list).
    """
    global status
    # Check the dump already exists. If so, remove it.
    if os.path.isfile(DB.DUMP_NAME.value):
        os.remove(DB.DUMP_NAME.value)

    # Get dump.
    dump_command = f"mysqldump -u{DB.LOGIN.value} -p{DB.PASSWORD.value}  {DB.NAME.value} > {DB.DUMP_NAME.value}"
    res = os.system(dump_command)
    if not res == 0:
        logger.critical('Error by creating DB dump!')
        this_method_name = sys._getframe().f_code.co_name
        status[this_method_name] = False
        return None   

    # Check the dump exists.
    if not os.path.isfile(DB.DUMP_NAME.value):
        logger.critical('Database dump cannot be received!')
        this_method_name = sys._getframe().f_code.co_name
        status[this_method_name] = False
        return None

    logger.success('DB dump ok.')
    return [DB.DUMP_NAME.value]
              

@logger.catch()
def get_tar_database():
    logger.trace("DB")
    archive_name = get_archive_db_name()
    db_dump_names = get_db_dump()
    if db_dump_names:
        with tarfile.open(archive_name, "w") as tar:
            for name in db_dump_names:
                tar.add(name)
        logger.success("DB ok!")
    return archive_name


def get_list_of_threads(mode='all'):
    """
    Returns list of threads according to the mode
    """

    threads = []    
    if mode == 'db_only':
        threads.append(asyncio.to_thread(get_tar_database))
        logger.trace("DB only")
    elif mode == 'files_only':
        threads.append(asyncio.to_thread(get_tar_files))   
        logger.trace("files only") 
    else:
        threads.append(asyncio.to_thread(get_tar_database))
        threads.append(asyncio.to_thread(get_tar_files))
        logger.trace("both files and DB")
    return threads


