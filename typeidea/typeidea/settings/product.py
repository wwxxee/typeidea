from .base import *  # NOQA


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jowon_blog_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '192.168.52.135',
        'PORT': 3306,
        'CONN_MAX_AGE': 60,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# ADMINS = MANAGERS = (('姓名',  '邮件地址'))

# EMAIL_HOST = '邮件smtp服务'
# EMAIL_HOST_USER = '邮箱登录名'
# EMAIL_HOST_PASSWORD = '邮箱登录密码'
# EMAIL_SUBJECT_PREFIX = 邮件标题前缀''
# DEFAULT_FROM_EMAIL = '邮件展示发件人地址'
# SERVER_EMAIL = '邮件服务器'

STATIC_ROOT = '/home/kali/Desktop/jowon/static_files_new/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(levelname)s %(asctime)s %(module)s:'
                      '%(funcName)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/tmp/logs/jowon.log',
            'formatter': 'default',
            'maxBytes': 1024 * 1024,  # 1M
            'backupCount': 5,
        },
    },
        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
            },
        }
}
