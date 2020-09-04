# 실서버 설정
from . import secret
from .base import *

### heroku ###

SECRET_KEY = secret.SECRET_KEY
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
ALLOWED_HOSTS = ['*']

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wisedb',
#         'USER': 'root',
#         'PASSWORD': 'schwisestudy',
#         'HOST': 'wisedb.cinqw7ouyrxc.ap-northeast-2.rds.amazonaws.com',
#         'PORT': 3306,
#         'OPTIONS': {
#             'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
#         }
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wisedb',
        'USER': 'b5d1e551889167',
        'PASSWORD': 'b5d1e551889167',
        'HOST': 'us-cdbr-east-02.cleardb.com',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}


WSGI_APPLICATION = 'config.wsgi.production.application'

