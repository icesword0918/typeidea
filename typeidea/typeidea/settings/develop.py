from.base import *  # NOQA


DEBUG = True

DATABASES = {
    'default': {

        # # 配置sqlite3数据库
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # 配置mysql数据库
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'Admin_0820!',
        'HOST': '152.136.194.98',
        'PORT': '3306',

    }
}