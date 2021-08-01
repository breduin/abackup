"""
Asynchronuos ftp-transfer using aioftp.
"""

import aioftp
import sys
from loguru import logger
from config import FTP, MAX_ARCHIVES
from status import status


@logger.catch()
async def delete_oldest_archive(client, file_type=''):
    """
    Deletes oldest archive file from ftp-server.
    """

    # Get current directory content
    dir_content = await client.list()
    files = {}

    # Looking for files with prefix 'file_type'
    for item in dir_content:
        filename = str(item[0])
        if filename.startswith(file_type):
            created_at = item[1]['modify']
            files[filename] = created_at

    # If number of files exceeds limit then remove the oldest one.
    if len(files) > MAX_ARCHIVES[file_type]:
        oldest_file = min(files, key=files.get)
        await client.remove(oldest_file)
        logger.success(f"Oldest arhive file {oldest_file} is removed.")
        await logger.complete()


@logger.catch()
async def upload_to_ftp_server(host, port, login, password, files):
    """
    Connects to ftp-server and uploads the archived files.
    """
    global status
    try:
        async with aioftp.Client.context(host, port, login, password) as client:
            logger.trace('Connected to the ftp-server.')
            await logger.complete()

            # Check the destination directory exists. If not, create it.
            is_dest_availabe = await client.exists(FTP.DESTINATION.value)
            if not is_dest_availabe:
                await client.make_directory(FTP.DESTINATION.value)

            await client.change_directory(FTP.DESTINATION.value)

            # Upload files until the queue is not empty.
            while len(files) > 0:
                file = files.pop()
                await client.upload(file)
                is_uploaded = await client.exists(file)
                if is_uploaded:
                    logger.success(f"File {file} is uploaded.")
                    await logger.complete()
                    # Check archive files for given type
                    # ('files' or 'db', files names start with that)
                    file_type = file.split('_')[0]
                    await delete_oldest_archive(client, file_type)
                else:
                    logger.error(f"File {file} is not found at remote server.")
                    await logger.complete()
                    this_method_name = sys._getframe().f_code.co_name
                    status[this_method_name] = False
            logger.success("Uploading ok.")
            await logger.complete()

    except aioftp.StatusCodeError as e:
        logger.error(f"Could not connect to the ftp-server. Expected: {e.expected_codes}, received: {e.received_codes}, info: {e.info}")
        this_method_name = sys._getframe().f_code.co_name
        status[this_method_name] = False
        
