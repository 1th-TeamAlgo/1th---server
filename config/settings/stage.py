# 테스트서버 설정
from .base import *
from . import secret
from django.db.backends.mysql.base import DatabaseWrapper

DatabaseWrapper.data_types['DateTimeField'] = 'datetime'

### heroku ###

SECRET_KEY = secret.SECRET_KEY
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
ALLOWED_HOSTS = ['*']


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

WSGI_APPLICATION = 'config.wsgi.stage.application'


