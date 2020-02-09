from djavue.settings.base import *

# Override base settings
DEBUG = False

user     = env('USER')
password = env('PASSWORD')
host     = env('HOST')
port     = env('PORT')
db       = env('DB_NAME')

DATABASES    = {}
DATABASE_URL = os.getenv('DATABASE_URL') or env('DB_URL')
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age = None)

try :
    from djavue.settings.local import *
except :
    raise Exception("You need to create your own local file settings")