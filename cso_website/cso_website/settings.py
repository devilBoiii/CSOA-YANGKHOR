"""
Django settings for cso_website project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIRS=os.path.join(BASE_DIR, "templates")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-96oc2rrhoir1g67jpo-izuk@)@f9mb^_5c-kjkgeui59vik*#c'

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
    #appName
    'cso_app',
    #CKEditor-5 App
    'django_ckeditor_5',    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cso_website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIRS],
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

WSGI_APPLICATION = 'cso_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "csoa_database",
        "USER": "root",
        "PASSWORD": "root",
        # "HOST": "host.docker.internal", uncomment this when you use docker
        "PORT": '3307'
        }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
    'django.contrib.auth.backends.ModelBackend',
]
AUTH_USER_MODEL = 'cso_app.users'


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Thimphu'  # Replace with your local time zone

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_FILES_DIRS = os.path.join(BASE_DIR, "static")
STATIC_ROOT = BASE_DIR / "static"


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_URL = '/sign_in/'  # This should match the URL of your login view

#Email Configurations 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'devilboi150@gmail.com'
EMAIL_HOST_PASSWORD = 'klxx yjlb jxqz ejti'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


CKEDITOR_5_CONFIGS = {
    'extends': {
        'toolbar': [
            'heading', '|', 'fontFamily', 'fontSize', '|', 
            'fontColor', 'fontBackgroundColor', '|', 
            'bold', 'italic', 'underline', '|', 
            'link', 'bulletedList', 'numberedList', '|', 
            'undo', 'redo'
        ],
        'fontFamily': {
            'options': [
                'default',
                'Arial, Helvetica, sans-serif',
                'Courier New, Courier, monospace',
                'Georgia, serif',
                'Lucida Sans Unicode, Lucida Grande, sans-serif',
                'Tahoma, Geneva, sans-serif',
                'Times New Roman, Times, serif',
                'Trebuchet MS, Helvetica, sans-serif',
                'Verdana, Geneva, sans-serif'
            ],
        },
        'fontSize': {
            'options': [
                'tiny',
                'small',
                'default',
                'big',
                'huge'
            ],
            'supportAllValues': False,
        },
        'fontColor': {
            'columns': 5,
            'documentColors': 10,
            'colors': [
                {
                    'color': 'hsl(0, 0%, 0%)',
                    'label': 'Black',
                },
                {
                    'color': 'hsl(0, 0%, 30%)',
                    'label': 'Dim gray',
                },
                {
                    'color': 'hsl(0, 0%, 60%)',
                    'label': 'Gray',
                },
                {
                    'color': 'hsl(0, 0%, 90%)',
                    'label': 'Light gray',
                },
                {
                    'color': 'hsl(0, 0%, 100%)',
                    'label': 'White',
                    'hasBorder': True,
                },
            ],
        },
    },
}
