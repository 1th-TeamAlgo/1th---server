# 개발 설정
from . import secret
from .base import *
from django.db.backends.mysql.base import DatabaseWrapper

DatabaseWrapper.data_types['DateTimeField'] = 'datetime'

SECRET_KEY = secret.SECRET_KEY
DEBUG = True
ALLOWED_HOSTS = ['*']

# WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_91058f0babf3969',
        'USER': 'b07cec7fd5b708',
        'PASSWORD': '527ea9e5',
        'HOST': 'us-cdbr-east-02.cleardb.com',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'wisestudy',
#         'USER': 'root',
#         'PASSWORD': 'schwisestudy',
#         'HOST': 'wisestudy.cinqw7ouyrxc.ap-northeast-2.rds.amazonaws.com',
#         'PORT': 3306,
#         'OPTIONS': {
#             'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
#         }
#     }
# }
WSGI_APPLICATION = 'config.wsgi.production.application'
