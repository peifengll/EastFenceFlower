"""
Django settings for EastFenceFlower project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mfehp%5vxk7@=3c&ql@eu@!i$&gi8=fj7c58+p@2svh=%y0(9v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '172.17.145.41',
    '*'
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'login',
    'users',
    'models',
    'orders',
    'flowers',
    'goods',
    'manager',
    'operate',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True  # 允许携带Cookie
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    [
        'http://127.0.0.1:*',
        'https://172.17.145.41:*',
    ]
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

## 全局配置
REST_FRAMEWORK = {
    # 设置所有接口都需要被验证
    'DEFAULT_PERMISSION_CLASSES': (
        # 设置所有接口都需要被验证
        'rest_framework.permissions.IsAuthenticated',  # 默认权限为验证用户
    ),
    # 用户登录的认证方式
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'libs.utils.jwt.MyJWTAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',  # 使用rest_framework_simplejwt验证身份
        # sesssion认证
        # 'rest_framework.authentication.SessionAuthentication',
        # 基本认证
        # 'rest_framework.authentication.BasicAuthentication',
    ]
}

# AUTH_USER_MODEL = 'login.Manager'

# 在 setting 配置认证插件的参数
SIMPLE_JWT = {
    # token有效时长(返回的 access 有效时长)
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=15),
    # token刷新的有效时间(返回的 refresh 有效时长)
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(seconds=20),
    # "TOKEN_OBTAIN_SERIALIZER": "libs.utils.jwtSerializer.LoginSerializer",
}

ROOT_URLCONF = 'EastFenceFlower.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'EastFenceFlower.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 数据库引擎配置
        'ENGINE': 'django.db.backends.mysql',
        # 数据库的名字
        'NAME': 'flower',
        # 'NAME': 'vote',
        # 数据库服务器的IP地址（本机可以写localhost或127.0.0.1）
        'HOST': '127.0.0.1',
        # 启动MySQL服务的端口号
        'PORT': 3306,
        # 数据库用户名和口令
        'USER': 'hellokitty',
        'PASSWORD': 'Hellokitty.618',
        # 数据库使用的字符集
        'CHARSET': 'utf8',
        # 数据库时间日期的时区设定
        'TIME_ZONE': 'Asia/Chongqing',

        'OPTIONS': {'charset': 'utf8mb4'},

    },
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Chongqing'
# Django是一个支持国际化和本地化的框架，因此Django项目的默认首页也是支持国际化的，我们可以
# 通过修改配置文件将默认语言修改为中文，时区设置为东八区。
# 找到修改前的配置（在settings.py文件第100行以后）。
USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# media_confige
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'static/media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
