"""
Django settings for apply project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '--v$_^*0r5(ok1^2sxdm4w_wwskvuv-z0tcop+yf1-m@+7p#5i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'gunicorn',
	'bootstrapform',
	'yard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'apply.urls'

WSGI_APPLICATION = 'apply.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'yard',                      # Or path to database file if using sqlite3.
    'USER': 'frankie',                      # Not used with sqlite3.
    'PASSWORD': 'frankie',                  # Not used with sqlite3.
    'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
  }
}

#'PASSWORD': 'frankie',                  # Not used with sqlite3.
#'HOST': 'archivione.caprj3rjkmkr.us-west-2.rds.amazonaws.com',                      # Set to empty string for localhost. Not used with sqlite3.
#'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

DOCS_URL = BASE_DIR + '/yard/static/docs/'


LOGGING = {
    'version': 1,
}

LOGIN_REDIRECT_URL="/"

