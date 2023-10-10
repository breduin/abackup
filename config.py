"""
Settings
"""
from enum import Enum
<<<<<<< HEAD
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
=======


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
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300

# Maximum number of archive files
MAX_DB_ARCHIVES = 5
MAX_FILES_ARCHIVES = 5

MAX_ARCHIVES = {
    PREFIX_TAR_DB: MAX_DB_ARCHIVES,
    PREFIX_TAR_FILES: MAX_FILES_ARCHIVES
    }

<<<<<<< HEAD
=======
# Should you be notified about errors by email?
# If True check EMAIL settings below.
ERROR_NOTIFICATION_BY_EMAIL = False    

>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
class FTP(Enum):
    """
    Parameters of remote FTP server
    """
<<<<<<< HEAD
    SERVER = env.str('FTP_SERVER')
    PORT = env('FTP_PORT')
    LOGIN = env.str('FTP_LOGIN')
    PASSWORD = env.str('FTP_PASSWORD')
    DESTINATION = env.str('FTP_DESTINATION')
=======
    SERVER = 'user.myjino.ru'
    PORT = 21
    LOGIN = 'user'
    PASSWORD = 'password'
    DESTINATION = '/tst'
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300


class DB(Enum):
    """
    Parameters for the data base
    """
<<<<<<< HEAD
    NAME = env.str('DB_NAME')
    LOGIN = env.str('DB_LOGIN')
    PASSWORD = env.str('DB_PASSWORD')
    DUMP_NAME = env.str('DB_DUMP_NAME')
    TYPE = env.str(
        'DB_TYPE',
        validate=OneOf(['postgresql', 'mysql'], error="DB type must be one of: {choices}")
        )
=======
    NAME = 'u1'
    LOGIN = 'u1'
    PASSWORD = 'Lfdfh5fgdf'
    DUMP_NAME = 'dump.sql'
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300

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
<<<<<<< HEAD
    SERVER = env.str('EMAIL_SERVER')
    PORT = env('EMAIL_PORT')
    LOGIN = env.str('EMAIL_LOGIN')
    PASSWORD = env.str('EMAIL_PASSWORD')
    FROM_ADDRESS = env.str('EMAIL_FROM_ADDRESS')
    TO_ADDRESS = env.str('EMAIL_TO_ADDRESS')
=======
    SERVER = 'smtp.yandex.ru'
    PORT = 465
    LOGIN = 'user@ya.ru'
    PASSWORD = 'vklk45;)HNw'
    FROM_ADDRESS = "user@ya.ru"
    TO_ADDRESS = "another_user@ya.ru"
>>>>>>> c7f9be07a18b99912cffaf15082ecf450c5e9300
