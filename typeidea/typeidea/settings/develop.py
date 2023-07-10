from .base import *  # NOQA


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jowon_blog_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.52.133',
        'PORT': 3306,
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

INSTALLED_APPS += [
    'silk',
]

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]


DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
}
