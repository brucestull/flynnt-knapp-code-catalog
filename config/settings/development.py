from config.settings.common import *
import os


DEBUG = True


ALLOWED_HOSTS = []


STATIC_ROOT = BASE_DIR / 'staticfiles'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Create your own `SECRET_KEY` here for use in Development.
# This one is provided here for user to get the DjangoCustomUserStarter up and running quickly.
    # Ideally, you would not run with `SECRET_KEY` exposed in development either.
        # You can set a `SECRET_KEY` on your development computer system.
        # Create a specific `SECRET_KEY` for development and use it in development only.
        # Create a specific `SECRET_KEY` for production and use it in production only.
SECRET_KEY = os.environ.get('SECRET_KEY')

# To create a new `SECRET_KEY`:
"""
    python .\manage.py shell
    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())
"""