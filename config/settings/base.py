# 공통 설정
import os
import datetime
from django.conf import settings

#카카오로그인
from ..settings.secret import SECRET_KEY


ROOT_URLCONF = 'config.urls'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    ## app
    'api',

    ##문서 자동화
    'drf_yasg',

    ## aws S3 이용
    'storages',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.UserJwtCheck.UserJwtCheckMiddleware',
    'middleware.ApiResponse.ResponseFormattingMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'config.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AWS S3

AWS_ACCESS_KEY_ID = 'AKIAWVQALOFDSUFI567Q' # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = '27Wdf+cuhopaNy/F+BQhpYS1+DVr/6TVN0ZoeAlJ' # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = 'ap-northeast-2'

###S3 Storages
AWS_STORAGE_BUCKET_NAME = 'wise-study-bucket' # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

### REST_FRAMEWORK
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = '/home/centos/wisestudy-server/static'
STATIC_URL = '/static/'
STARTFILES_DIRS = (
    os.path.join(BASE_DIR,'static')	
)
APPEND_SLASH = False
