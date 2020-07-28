# 개발 설정
import os

from .base import *

SECRET_KEY = '78si$+oqq57vf)*eykl=-@40359g-uuz)-yh+4dja!^!-9^(h$'
DEBUG = True
ALLOWED_HOSTS = []

# WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
