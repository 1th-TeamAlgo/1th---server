# 실서버 설정
from . import secret
from .base import *


SECRET_KEY = secret.SECRET_KEY
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wisestudy',
        'USER': 'root',
        'PASSWORD': 'schwisestudy',
        'HOST': 'wisestudy.cinqw7ouyrxc.ap-northeast-2.rds.amazonaws.com',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

CACHES = {
    'default' : {
        'BACKEND' : 'django_redis.cache.RedisCache',
        'LOCATION' : 'redis://ec2-3-34-134-147.ap-northeast-2.compute.amazonaws.com:6379/0',
	'OPTIONS':{
            'CLIENT_CLASS':'django_redis.client.DefaultClient',
        }
    }
}


WSGI_APPLICATION = 'config.wsgi.production.application'

