# 테스트서버 설정
from .base import *

### heroku ###
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '78si$+oqq57vf)*eykl=-@40359g-uuz)-yh+4dja!^!-9^(h$')
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
ALLOWED_HOSTS = ['*']

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wise_testDB',
        'USER': 'b07cec7fd5b708',
        'PASSWORD': '527ea9e5',
        'HOST': 'us-cdbr-east-02.cleardb.com',
        'PORT': 3306,
        # 'OPTIONS': {
        #     'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        # }
    }
}

WSGI_APPLICATION = 'config.wsgi.application'

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
