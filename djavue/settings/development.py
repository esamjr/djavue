from djavue.settings.base import *
import environ
env = environ.Env()
environ.Env.read_env('./.env')

# Override base settings
ALLOWED_HOSTS = [
    '127.0.0.1', 'localhost'
]

user     = env('USER')
password = env('PASSWORD')
host     = env('HOST')
port     = env('PORT')
db       = env('DB_NAME')

DATABASES    = {}
DATABASE_URL = os.getenv('DATABASE_URL') or env('DB_URL')
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age = None)

DEBUG = True

try :
    from djavue.settings.local import *
except :
    raise Exception("You need to create your own local file settings")