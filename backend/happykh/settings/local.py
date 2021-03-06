"""
Django settings for happykh project on local machine(for deployment).

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

FRONT_URL_PREFIX = 'http://127.0.0.1:8080/#/'

ALLOWED_HOSTS = '*'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'happykh',
        'USER': 'localadmin',
        'PASSWORD': 'localpassword',
        'HOST': 'localhost',
        'PORT': '',
    }
}

CORS_ORIGIN_REGEX_WHITELIST = (
    # For Client
    r'http://localhost*',
    r'http://127.0.0.1:*',
    # For Testing Environment
    r'null',
)
