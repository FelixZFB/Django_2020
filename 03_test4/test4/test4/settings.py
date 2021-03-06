"""
Django settings for test4 project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# 设置项目文件夹系统路径，即使项目文件夹位置移动，项目中的使用的文件夹路径是和BASE_DIR进行拼接的，也不会受到影响
# 下面设置中TEMPLATES模板路径和DATABASES数据库路径都是使用BASE_DIR进行拼接的
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!f6f*6hrowbb498s^qg_nnoi(j!p(jf5*z$wxwww&w6(-%f8#&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest', # 注册安装应用
    # 'haystack', # 注册安装全文检索框架应用
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware', # 默认打开csrf防护，只针对post表单提交，表单里面需要加上{% csrf_token %}标签
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'booktest.middleware.BlockIPSMiddleware', # 注册自定义的中间件类
    'booktest.middleware.TestMiddleware', # 注册自定义的中间件类
]

ROOT_URLCONF = 'test4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # 配置模板文件夹路径
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

WSGI_APPLICATION = 'test4.wsgi.application'


# 配置搜索引擎haystack
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         #使用whoosh引擎
#         'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
#         #索引文件路径
#         'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
#     }
# }

# 当添加、修改、删除数据时，自动生成索引
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# django默认sqlite3轻量化数据库
# 自定义使用mysql数据库，使用前要先启动数据库服务
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql', #使用mysql数据库
        'NAME': 'django_test4', #使用的数据库database的名字，已经提取创建好
        'USER': 'root', #数据库登录用户名，默认使用管理员root
        'PASSWORD': '00116656', #数据库登录密码,数据库安装时候设置的用户密码
        'HOST': 'localhost', #数据库所在主机的IP地址，本机直接用localhost
        'PORT': '3306', #数据库端口，默认就是3306
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans' #使用中国语言

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai' #使用中国上海时间，django设计时候没有北京时间

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


# 设置访问静态文件对应的url地址，默认是static，我们可以对其修改
STATIC_URL = '/static/'
# 将默认的static修改为abc(相当于给静态文件夹重命名了)，此时模板html文件源码中就要使用abc，使用static就访问不到静态文件了
# STATIC_URL = '/abc/'


# 设置静态文件存放的物理文件夹目录
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # 设置静态文件的保存目录


# 设置上传文件存放的目录
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
