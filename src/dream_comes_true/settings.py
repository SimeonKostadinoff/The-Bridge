"""
Django settings for dream_comes_true project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(04sk)uwq&)iqj1e7b&ob%dw4pnouvqv5r#pgeqi%h$vok6cfc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth_user',
    'customer',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'organisation', 
    'partnership',
    'posts',
    'rest_framework',
    'reversion',
    'rest_api',
    'imagekit',
    'userprofile',
    'webpack_loader',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dream_comes_true.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', 'allauth_user/templates', 'userprofile/templates', 'customer/templates', 'organisation/templates', 'posts/templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                #"allauth.account.context_processors.account",
                #"allauth.socialaccount.context_processors.socialaccount",
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
     # Needed to login by username in Django admin and to ensure compatibility with other packages
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods
    'allauth.account.auth_backends.AuthenticationBackend',
)

WSGI_APPLICATION = 'dream_comes_true.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# change the default sqlite3 database with postgresql database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbdreamproject',
        'USER': 'dreamprojectadminuser',
        'PASSWORD': 'dreamprojectpass',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/app/static/'
MEDIA_URL = '/media/'

# locate the static files (css, js, images)
STATICFILES_DIRS = [
    # in the console type : python3 manage.py collectstatic and the files from static folder will be transfered into static_cdn folder
    os.path.join(BASE_DIR, 'app/static'),
]

# STATIC_ROOT - folder that collects all static files
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn')
# MEDIA ROOT - folder that collects all media files (files uploaded by the user)
#MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')
# for development it will stay like this
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

##################
# Configurations used for AllAuth
#################

# Redirect to base.html when user log in
LOGIN_REDIRECT_URL = '/'

# Ensure the SITE_ID is defined 
SITE_ID = 1

# Ensure EMAIL_BACKEND is set so allauth can proceed to send confirmation emails
# Set to console for development/testing
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

# Custom allauth settings
# Use email as the primary identifier
ACCOUNT_AUTHENTICATION_METHOD = 'email' 
ACCOUNT_EMAIL_REQUIRED = True
# Make email verification mandatory to avoid junk email accounts / CHANGE TO 'mandatory' 
ACCOUNT_EMAIL_VERIFICATION = 'none' 
# Eliminate need to provide username, as it's a very old practice
ACCOUNT_USERNAME_REQUIRED = False

# Change this!!! no confirmation required via email
ACCOUNT_CONFIRM_EMAIL_ON_GET = False

# Disable the intermediate signout page from django allauth
ACCOUNT_LOGOUT_ON_GET = True

# Override forms
ACCOUNT_FORMS = {
    'signup': 'allauth_user.forms.SignupFormOverride',
    'login':'allauth_user.forms.LoginFormOverride'
}

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/local/',  # end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'app/webpack-stats.json'),
    }
}

# REST API configurations
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}
