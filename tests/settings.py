# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SITE_ID = 1
SECRET_KEY = "44444444444444444444444444444444444444444444444444"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
]

MIDDLEWARE = (
    'web_exceptions.middleware.WebExceptionsMiddleware',
)

TEST_RUNNER = 'rainbowtests.test.runner.RainbowDiscoverRunner'
