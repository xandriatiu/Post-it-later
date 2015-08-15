from __future__ import (
    absolute_import,
)

import os


SECRET_KEY = 'wvi23j*gv)x&jc=fkcqf7g@^%e77d0_mtovpsz77wu@6_mej3j'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    # django admin theme
    'flat',

    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    # third party apps
    'easy_thumbnails',
    'bootstrapform',
    'djcelery',
    'kombu.transport.django',
    'social.apps.django_app.default',
    'fixture_magic',
    'paypal.standard',
    'paypal.pro',

    # local apps
    'users',
    'queue',
    'unlockpaidfeatures',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'conf.urls'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',

)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'users.pipeline.save_profile',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

SOCIAL_AUTH_FACEBOOK_KEY = '986559941408186'
SOCIAL_AUTH_FACEBOOK_SECRET = 'a3c820b1665b39fe3df81870b0799f5e'
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}
SOCIAL_AUTH_FACEBOOK_SCOPE = ['publish_actions']

SOCIAL_AUTH_TWITTER_KEY = '4SSmH4zcFhOxLr7LZBMS1jzdD'
SOCIAL_AUTH_TWITTER_SECRET = 'ts3klVMLrttxhSnofN79pKi3YSx2exZglmDwB1tKnztZpZnpqV'

PAYPAL_TEST = True
PAYPAL_WPP_USER = "yoni_0326_api1.yahoo.com"
PAYPAL_WPP_PASSWORD = "7CJ8BHSF7856NVQ8"
PAYPAL_WPP_SIGNATURE = "A30OYQ0RUJGyss-TGAD-d8NcnL02AK1IeToIPymys74suuZgndJXC6ul"
PAYPAL_RECEIVER_EMAIL = ""

SOUTH_DATABASE_ADAPTERS = {
     'default': "south.db.postgresql_psycopg2"
 }


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'assets', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = '/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'frontend', 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets', 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'frontend', 'media')

# SETTINGS FOR THIRD PARTY APPS
THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (25, 25), 'crop': True},
        'avatar-bg': {'size': (100, 100), 'crop': True},
        'avatar-xl': {'size': (220, 220), 'crop': True},
        'avatar-xxl': {'size': (420, 420), 'crop': True},
    },
}


try:
    from conf.local_settings import *
except ImportError:
    pass
