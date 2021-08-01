"""
Settings
"""
from enum import Enum


# Tuple of files and directories to be archived
FILES_TO_ARCHIVE = (
    '/var/www/u1/data/www/tst/crm',
    '/var/www/u1/data/www/tst/static',
    '/var/www/u1/data/www/tst/env',
    '/var/www/u1/data/www/tst/requirements.txt',
    '/var/www/u1/data/www/tst/passenger_wsgi.py'
)

# Prefix for tar names
PREFIX_TAR_FILES = 'files'
PREFIX_TAR_DB = 'db'

# Maximum number of archive files
MAX_DB_ARCHIVES = 5
MAX_FILES_ARCHIVES = 5

MAX_ARCHIVES = {
    PREFIX_TAR_DB: MAX_DB_ARCHIVES,
    PREFIX_TAR_FILES: MAX_FILES_ARCHIVES
    }

class FTP(Enum):
    """
    Parameters of remote FTP server
    """
    SERVER = 'user.myjino.ru'
    PORT = 21
    LOGIN = 'user'
    PASSWORD = 'password'
    DESTINATION = '/tst'


class DB(Enum):
    """
    Parameters for the data base
    """
    NAME = 'u1'
    LOGIN = 'u1'
    PASSWORD = 'Lfdfh5fgdf'
    DUMP_NAME = 'dump.sql'

    @classmethod
    def values(cls):
        """
        Returns list of values of each class member.
        """
        return [x.value for _, x in cls.__members__.items()]


class EMAIL(Enum):
    """
    Parameters of SMTP server
    """
    SERVER = 'smtp.yandex.ru'
    PORT = 465
    LOGIN = 'user@ya.ru'
    PASSWORD = 'vklk45;)HNw'
    FROM_ADDRESS = "user@ya.ru"
    TO_ADDRESS = "another_user@ya.ru"