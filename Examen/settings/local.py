from .base import *

SECRET_KEY = 'django-insecure-x!x@*yr@p#^w10&a6tn2btbg15y%3pz*1!k1l-lfn8cbpx7v+i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # python manage.py migrate
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bd_restaurant_app',
        'USER': 'postgres',
        'PASSWORD': 'Dieguito17',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

