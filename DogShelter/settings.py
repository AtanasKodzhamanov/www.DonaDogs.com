"""
Django settings for DogShelter project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

import dj_database_url

CSRF_TRUSTED_ORIGINS = [
    "https://*.donadogs.up.railway.app",
    "https://*.donadogs.com",
    "https://*.donadogs.org",
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ["SECRET_KEY"]
RECAPTCHA_PUBLIC_KEY = os.environ["SITE_KEY"]
RECAPTCHA_PRIVATE_KEY = os.environ["SECRET_KEY_CAPTCHA"]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["www.donadogs.org", "www.donadogs.com", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "captcha",
    "DogShelter.web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # translation
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = "DogShelter.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
            ],
            "libraries": {
                "shuffle": "DogShelter.web.templatestags.shuffle",
                "truncatetext": "DogShelter.web.templatestags.truncatetext",
                "field_loop": "DogShelter.web.templatestags.field_loop",
                "get_attribute": "DogShelter.web.templatestags.get_attribute",
            },
        },
    },
]

WSGI_APPLICATION = "DogShelter.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# export POSTGRES_USERNAME="username"
# echo $POSTGRES_USERNAME

# go to ~/.bashrc
# append this command ---> export POSTGRES_USERNAME="username"
# append this command ---> export POSTGRES_PASSWORD="password"

# Windows "Edit the system environment variables"

'''
POSTGRES_ENGINE = os.environ["POSTGRES_ENGINE"]
POSTGRES_USERNAME = os.environ["POSTGRES_USERNAME"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_NAME = os.environ["POSTGRES_NAME"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]
POSTGRES_PORT = os.environ["POSTGRES_PORT"]

# Railway.app setting
DATABASES = {
    "default": {
        "ENGINE": POSTGRES_ENGINE,
        "NAME": POSTGRES_NAME,
        "USER": POSTGRES_USERNAME,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
    }
}
'''

DATABASE_URL = os.environ['DATABASE_URL_DONADOGS']

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ("en", "English"),
    ("bg", "Bulgarian"),
]

# fix paths a bit
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "staticfiles/static/"),)
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
