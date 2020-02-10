#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ
import dotenv

def main() :
    dotenv.read_dotenv(override = True)
    env = environ.Env(DEBUG = (bool, False))
    environ.Env.read_env('./.env')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        try :
            import django
        except ImportError :
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
