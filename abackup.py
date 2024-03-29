"""
Asynchronuos script to backup a site using aioftp and asyncio.

Calls system command 'tar' to archive the files, dumps database,
then loads the archive to remote server (another hosting).
"""
import asyncio
from loguru import logger

from abemail import backup_email
from collections import deque
from config import FTP, LOGS_PATH, SITE_NAME
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


@logger.catch()
async def main():
    """
    Main function to start the programm.
    Initializes program's blocks.
    """
    global status

    # queue of files to be archived
    files_to_upload = deque()

    logger.info(f'Backup of {SITE_NAME} database.')
    logger.trace("Archiving ...")
    # Tasks to archive files and database dump
    list_of_threads = get_list_of_threads()

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
    clear_garbage(tar_names)

    # Check the workflow status. If it's not empty, send an error email.
    if len(status) > 0:
        backup_email()


if __name__ == '__main__':
    asyncio.run(main())
