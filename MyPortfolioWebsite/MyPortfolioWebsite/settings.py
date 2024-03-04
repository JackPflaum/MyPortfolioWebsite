"""
Django settings for MyPortfolioWebsite project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# load_dotenv loads environmental variables into os.environ dictionary
load_dotenv(find_dotenv())
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG:
    # during development
    ALLOWED_HOSTS = []
else:
    # during production
    ALLOWED_HOSTS = ['jackpflaum.com', 'www.jackpflaum.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jacks_website',
    'widget_tweaks',

    'storages',    # utilising django-storages package for defining storage backend for files
    'boto3',    # AWS SDK (Software Development Kit) to help python project interact with AWS
    'django_ses',    # AWS SES integration with django
]


########### AWS Configuration (using S3 buckets to store and access media and static files) ###########

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']    # keys for external access to S3 bucket
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'jack-pflaum-portfolio-website'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.ap-southeast-2.amazonaws.com'  # for serving files from S3 bucket

AWS_S3_FILE_OVERWRITE = True    # files will be overwritten if names are the same

# storage of static and media files during development and during production
if DEBUG:
    # static and media files stored on local computer during development

    # Static files (CSS, JavaScript, Images)
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    # media files (uploaded images, videos, etc.)
    MEDIA_URL = '/media/'    # specifies the base URL that will be used to serve up media files
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    # defines absolute file path where media files will be stored
else:
    # static and media files are stored and served from AWS S3 bucket during production

    # Static files (CSS, JavaScript, images)
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'    # storage backend for managing static files
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'    # this is where static files will be sent to and located

    # Media files (user uploads)
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'    # storage backend for managing media files
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/'    # this is where user uploaded files will be sent to and located


# WhiteNoise is dedicated module to collect static files for production on Render.com
# I have opted for storing static files in AWS S3 bucket and therefore the below code is
# commented out as reference if I change my mind in the future.
"""
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
"""


########### Email configuration for contact form ###########

if DEBUG:
    # development configuration
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # AWS SES (Simple Email Service) configuration in production (sending user messages to email account)
    EMAIL_BACKEND = 'django_ses.SESBackend'
    AWS_SES_REGION_NAME = 'ap-southeast-2'
    AWS_SES_REGION_ENDPOINT = 'email.ap-southeast-2.amazonaws.com'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',     
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MyPortfolioWebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MyPortfolioWebsite.wsgi.application'


###########Database Configuration#################

# running PostgreSQL on local computer and host site (Render.com)
import dj_database_url

# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if not DEBUG:
    # production environment PostgreSQL
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    # development environemnt PostgreSQL

    # use line below in terminal to dump local PostgreSQL database data to file:
    # pg_dump -U postgre_username -h postgre_hostname -d db_name -W > datadump.sql
    # if not encoded in UTF-8 then open in notepad and save in UTF-8 encoding.

    # use line below to seed external render.com PostgreSQL database with datadump.sql file
    # psql -h render_host -U render_user -d render-database -W -f datadump.sql

    # make sure you are in the location of datadump.sql file when running commands.

    DATABASES = {
        'default': {
            # previously running on sqlite database during development
            # 'ENGINE': 'django.db.backends.sqlite3',
            # 'NAME': BASE_DIR / 'db.sqlite3',
            
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            'PORT': os.environ.get('DB_PORT', 5432),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
