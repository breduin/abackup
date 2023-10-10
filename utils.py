import os
import sys
from loguru import logger
from config import DB
from status import status


@logger.catch()
def get_mode() -> str:
    """
    Returns mode in accordance of the argument in command which runs the script.
    """
    
    # Check the argument in command line
    try:
        mode = sys.argv[1]
    except IndexError:
        mode = 'db_only'
    return mode


@logger.catch()
def delete_files(files=[]):
    """
    Deletes files on the server from the list 'files'.
    """
    global status
    if files:
        for file in files:
            try:
                os.remove(file)
                logger.info(f"Tar file '{file}' is removed.")
            except FileNotFoundError:
                logger.error(f"Tried to delete '{file}', file not found.")
                this_method_name = sys._getframe().f_code.co_name
                status[this_method_name] = False


@logger.catch()
def clear_garbage(files):
    """
    Removes tar and dump files in accordance with the mode
    """
    mode = get_mode()
    if files:
        delete_files(files=files)
    if not mode == 'files_only':
        delete_files([DB.DUMP_NAME.value])
