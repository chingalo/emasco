import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'emasco',  
        'USER': 'emasco',
        'PASSWORD': 'emasco',
    }
}

TIME_ZONE = 'Africa/Dar_es_Salaam'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"
STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

SECRET_KEY = ')v5p2a2s-rgdq0f+p%(sv@7og(6+y)r5$kf4xsom7wfh_#l5@o'


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'emascouser',
    'contacts',
    'portfolio',
    'administration',
    'services',
    'missionVission',
    'aboutUs',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_DIRS = (
       os.path.join(PROJECT_PATH, "templates"),
)  

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    
)

ROOT_URLCONF = 'emasco.urls'

WSGI_APPLICATION = 'emasco.wsgi.application'


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}



# Allow all host headers
ALLOWED_HOSTS = ['*']

#email configrarion
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_IMAP_HOST = 'imap.gmail.com'
EMAIL_PORT = "587"
EMAIL_HOST_USER = 'emascocompany@gmail.com'
EMAIL_HOST_PASSWORD = 'chingalo'
EMAIL_USE_TLS = True
EMAIL_SENDER = 'emascocompany@gmail.com'
EMAIL_SSL = True


