# 개발 설정
import os

from . import secret
from .base import *

SECRET_KEY = secret.SECRET_KEY
DEBUG = True
ALLOWED_HOSTS = []

# WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
