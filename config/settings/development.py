#개발 설정
import os

from.base import *

#dev SECRET KEY 노출되어도  무방, 실서버와는 다름
SECRET_KEY = '78si$+oqq57vf)*eykl=-@40359g-uuz)-yh+4dja!^!-9^(h$'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += [

]

# WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE += [

]

# ROOT_URLCONF = 'config.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'config.wsgi.application'
#
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
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
# STATIC_URL = '/static/'
