"""
Settings
"""
from enum import Enum
from environs import Env
from marshmallow.validate import OneOf


env = Env()
env.read_env('.env', recurse=False)


# Logging path
LOGS_PATH = 'logs/main.log'


# Tuple of files and directories to be archived
FILES_TO_ARCHIVE = env.list('FILES_TO_ARCHIVE')


# Prefix for tar names
PREFIX_TAR_FILES = env.str('PREFIX_TAR_FILES')
PREFIX_TAR_DB = env.str('PREFIX_TAR_DB')
SITE_NAME = env.str('SITE_NAME')


# Maximum number of archive files
MAX_ARCHIVES = {
    PREFIX_TAR_DB: env('MAX_DB_ARCHIVES'),
    PREFIX_TAR_FILES: env('MAX_FILES_ARCHIVES')
    }


class FTP(Enum):
    """
    Parameters of remote FTP server
    """
    SERVER = env.str('FTP_SERVER')
    PORT = env('FTP_PORT')
    LOGIN = env.str('FTP_LOGIN')
    PASSWORD = env.str('FTP_PASSWORD')
    DESTINATION = env.str('FTP_DESTINATION')


class DB(Enum):
    """
    Parameters for the data base
    """
    NAME = env.str('DB_NAME')
    LOGIN = env.str('DB_LOGIN')
    PASSWORD = env.str('DB_PASSWORD')
    DUMP_NAME = env.str('DB_DUMP_NAME')
    TYPE = env.str(
        'DB_TYPE',
        validate=OneOf(['postgresql', 'mysql'], error="DB type must be one of: {choices}")
        )

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
    SERVER = env.str('EMAIL_SERVER')
    PORT = env('EMAIL_PORT')
    LOGIN = env.str('EMAIL_LOGIN')
    PASSWORD = env.str('EMAIL_PASSWORD')
    FROM_ADDRESS = env.str('EMAIL_FROM_ADDRESS')
    TO_ADDRESS = env.str('EMAIL_TO_ADDRESS')
