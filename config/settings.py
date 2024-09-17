"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os.path
from pathlib import Path
# from environs import Env
from django.urls import reverse_lazy
from decouple import config
from django.contrib.messages import constants as msg_cons


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY")
SECRET_KEY = 'django-insecure-&bq6*%7zxk^ycd^ccwiat&nwgw^58))9m-ej93q^g3!756_5_n'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = config("DJANGO_DEBUG", cast=bool)
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
    'django.contrib.humanize',


    # third-party
    'crispy_forms',
    'allauth',
    'allauth.account',
    'rosetta',
    'jalali_date',
    'ckeditor',
    'azbankgateways',

    # My_Apps
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'gateways.apps.GatewaysConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                #Custom
                'cart.context_processor.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data/db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    # 'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'arminam3214@gmail.com'
# EMAIL_HOST_PASSWORD = 'tskcywucarycyxxw'


AUTH_USER_MODEL = 'accounts.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fa'

LANGUAGES = (
    ('en', 'English'),
    ('fa', 'Persian'),
)

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'pages:home'
LOGOUT_REDIRECT_URL = 'pages:home'

CRISPY_TEMPLATE_PACK = 'bootstrap4'


#all-auth-setting
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

#messages
MESSAGE_TAGS = {
    msg_cons.ERROR: 'alert alert-danger',
    msg_cons.SUCCESS: 'alert alert-success',
    msg_cons.WARNING: 'alert alert-warning',
    msg_cons.INFO: 'alert alert-info',
}

#Localization
# LOCALE_PATHS = [
# 'products/locale'
    # os.path.join(BASE_DIR, 'products/locale'),
#     os.path.join(BASE_DIR, 'cart/locale'),
#     os.path.join(BASE_DIR, 'cart/locale'),
    # os.path.join(BASE_DIR, 'locals'),
# ]


# default settings
JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%Y/%m/%d',
        'datetime': '%H:%M:%S _ %Y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}


#Gate Ways

AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
       # 'ZARINPAL': {
       #     'MERCHANT_CODE': config('ZARINPAL'),
       # },
       'IDPAY': {
           # 'MERCHANT_CODE': config('IDPAY'),
           'MERCHANT_CODE': '6cbce8a7-ec8f-41d1-bf32-136012ebf49c',
           'METHOD': 'GET',  # GET or POST
           'X_SANDBOX': 1,  # 0 disable, 1 active
       },

   },
   'DEFAULT': 'IDPAY',
   # 'CURRENCY': 'IRR', # اختیاری
   # 'TRACKING_CODE_QUERY_PARAM': 'tc', # اختیاری
   'TRACKING_CODE_LENGTH': 16, # اختیاری
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # اختیاری
   'BANK_PRIORITIES': [
       'ZARINPAL',
       'IDPAY',
       # and so on ...
   ], # اختیاری
}


