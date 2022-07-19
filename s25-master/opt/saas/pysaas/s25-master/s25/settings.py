"""
Django settings for s25 project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5cgwwp#mio9=kq@rfi!oi2h=b=wcd0_2p!qf33@)k%x4kdg!0*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01.apps.App01Config',
    'web.apps.WebConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'web.middleware.auth.AuthMiddleware'
]

ROOT_URLCONF = 's25.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 's25.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# datetime.datetime.now() / datetime.datetime.utcnow() => utc时间
# TIME_ZONE = 'UTC'

# datetime.datetime.now() - 东八区时间 / datetime.datetime.utcnow() => utc时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 影响自动生成数据库时间字段；
#       USE_TZ = True，创建UTC时间写入到数据库。
#       USE_TZ = False，根据TIME_ZONE设置的时区进行创建时间并写入数据库
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# ######## sms  ########

# 腾讯云短信应用的 app_id
TENCENT_SMS_APP_ID = 6666666666

# 腾讯云短信应用的 app_key
TENCENT_SMS_APP_KEY = "6666666666666666666666"

# 腾讯云短信签名内容
TENCENT_SMS_SIGN = "Python之路"

TENCENT_SMS_TEMPLATE = {
    'register': 548760,
    'login': 548762
}

TENCENT_COS_ID = "COS的secret_id"
TENCENT_COS_KEY = "COS的secret_key"

# ########### 登录白名单：无需登录就可以访问的页面 ###########
WHITE_REGEX_URL_LIST = [
    "/register/",
    "/send/sms/",
    "/login/",
    "/login/sms/",
    "/image/code/",
    "/index/",
    "/price/",
]

try:
    from .local_settings import *
except ImportError:
    pass
