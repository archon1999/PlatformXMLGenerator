import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y5kn#ef)ln!)yz8&&@ou$%1c3mxx5uj^c&++fg=1w22t=jayv2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.backend',
    'apps.frontend',
    'apps.frontend.templatetags.custom_tags',
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

ROOT_URLCONF = 'core.urls'
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'


STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

JET_SIDE_MENU_COMPACT = True


AUTH_USER_MODEL = 'backend.User'


DEFAULT_FROM_EMAIL = 'nazarbek.baltabaev@gmail.com'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nazarbek.baltabaev@gmail.com'
EMAIL_HOST_PASSWORD = 'kakaujuj1234'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_DefaultToolbarConfig': [
            {
                'name': 'code',
                'items': ['Mathjax', 'CodeSnippet'],
            },
            {
                'name': 'format',
                'items': ['Format', 'FontSize'],
            },
            {
                'name': 'basicstyles',
                'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                          'Superscript', ],
            },
            {
                'name': 'clipboard',
                'items': ['Undo', 'Redo', ],
            },
            {
                'name': 'paragraph',
                'items': ['NumberedList', 'BulletedList', 'Outdent', 'Indent',
                          'HorizontalRule', 'JustifyLeft', 'JustifyCenter',
                          'JustifyRight', 'JustifyBlock', ],
            },
            {
                'name': 'extra',
                'items': ['Link', 'Unlink', 'Blockquote', 'Image', 'Table'],
            },
            {
                'name': 'source',
                'items': ['Maximize', 'Source', ],
            },
        ],
        'title': False,

        'toolbar': 'DefaultToolbarConfig',

        'format_tags': 'p;pre;h1;h2;h3;h4;h5;h6',

        'removeDialogTabs': ';'.join([
            'image:advanced',
            'image:Link',
            'link:upload',
            'table:advanced',
            'tableProperties:advanced',
        ]),
        'linkShowTargetTab': False,
        'linkShowAdvancedTab': False,

        'height': '500px',
        'width': '1000px',
        'forcePasteAsPlainText ': True,

        'mathJaxClass': 'mathjax-latex',
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_SVG',
        'tabSpaces': 4,
        'extraPlugins': 'mathjax, codesnippet',

        'codeSnippet_theme': 'atelier-health.light',
        'codeSnippet_languages': {
            'python': 'Python',
        },
    }
}
