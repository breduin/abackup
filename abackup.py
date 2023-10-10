"""
Asynchronuos script to backup a site using aioftp and asyncio.

<<<<<<< HEAD
Calls system command 'tar' to archive the files, dumps database,
then loads the archive to remote server (another hosting).
"""
import asyncio
from loguru import logger

from abemail import backup_email
from collections import deque
from config import FTP, LOGS_PATH
from ftp import upload_to_ftp_server
from make_archive import get_list_of_threads
from status import status
from utils import clear_garbage


logger.add(
    LOGS_PATH,
    format="{time} {level} {message}",
    rotation='100Kb',
    level="INFO",
    )

=======
Calls system command 'tar' to archive the files, 'mysqldump' to create database dump,
then uploads the archived files to remote server (another hosting) via ftp.
"""

import asyncio
import sys
from loguru import logger
from config import FTP, DB, ERROR_NOTIFICATION_BY_EMAIL
from collections import deque
from make_archive import get_list_of_threads
from utils import clear_garbage
from ftp import upload_to_ftp_server
from abemail import backup_email
from status import status

logger.add('logs/main.log', format="{time} {level} {message}", rotation='100Kb', level="INFO")
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300

@logger.catch()
async def main():
    """
    Main function to start the programm.
    Initializes program's blocks.
    """
<<<<<<< HEAD
    global status

    # queue of files to be archived
    files_to_upload = deque()

    logger.trace("Archiving ...")
    # Tasks to archive files and database dump
    list_of_threads = get_list_of_threads()
=======
    
    # workflow status
    global status

    # Mode says which objects must be archived: DB dump, source files or both.
    try:
        mode=sys.argv[1]
    except IndexError:
        mode = 'all'

    # queue of files to be archived
    files_to_upload = deque()
    
    logger.trace("Archiving ...")
    # Tasks to archive files and database dump
    list_of_threads = get_list_of_threads(mode=mode)
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300

    tar_names = await asyncio.gather(*list_of_threads)

    # Clear names list, removing None elements if exist
    tar_names = [name for name in tar_names if name]

    files_to_upload.extend(tar_names)
    logger.trace("Ok.")

    logger.trace("Uploading ...")

    # Connect to the ftp-server and upload the archived files.
    await upload_to_ftp_server(host=FTP.SERVER.value,
                               port=FTP.PORT.value,
                               login=FTP.LOGIN.value,
                               password=FTP.PASSWORD.value,
                               files=files_to_upload)

    # Remove archived and dump files on the server site.
<<<<<<< HEAD
    clear_garbage(tar_names)

    # Check the workflow status. If it's not empty, send an error email.
    if len(status) > 0:
=======
    clear_garbage(mode=mode, files=tar_names)

    # Check the workflow status. If it's not empty, send an error email.
    if len(status) > 0 and ERROR_NOTIFICATION_BY_EMAIL:
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
        backup_email()


if __name__ == '__main__':
    asyncio.run(main())
<<<<<<< HEAD
=======

>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
