"""
Django settings for Crowdcams project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
SESSION_COOKIE_SERCURE = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f*km22)e)&@@ngb#yltt=+)0%dx+e_c*dsd^z-02w92db1kocs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ["crowdcams.org","www.crowdcams.org", "127.0.0.1"]

#Test Domain 127.0.0.1
#RECAPTCHA_PUBLIC_KEY = '6LcezPASAAAAAGu4nc6H7zLTSeb72LwKBk4PM7ya'
#RECAPTCHA_PRIVATE_KEY = '6LcezPASAAAAAAT4y4ap0632StvvsFrccE3JAAvU'

#http://crowdcams.org
RECAPTCHA_PUBLIC_KEY = '6Leo0_ASAAAAAJ8Lz9Vz8NqN5-DKBXvOuTPDSTJw'
RECAPTCHA_PRIVATE_KEY = '6Leo0_ASAAAAADrxROA-VGWsSlbsFTsfL4Ux99JH'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web_app',
    'captcha',
    'djcelery'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Crowdcams.urls'

WSGI_APPLICATION = 'Crowdcams.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

# Template files

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'