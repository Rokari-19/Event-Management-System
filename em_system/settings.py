from pathlib import Path
import os
import datetime
import environ
from celery import Celery

# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
import cloudinary_storage

env = environ.Env(
    DEBUG=(bool,False)
)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app',
  ]


app = Celery('em_system')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # installed apps
    'core',
    'accounts',
    'calendarApp',
    # drf apps
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    
    # cloud storage apps
    # 'cloudinary',
    # 'cloudinary_storage',

    # login mamagement
    # 'djoser',
    # no need for djoser again
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication', 
    ],
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080"
]
# CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'em_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'em_system.wsgi.application'
ASGI_APPLICATION = 'em_system.asgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# WSGI_APPLICATION = 'em_system.wsgi.application'


'''postgresdb setup for amazon rds'''

DATABASES = {
    "default":{
        "ENGINE": 'django.db.backends.postgresql_psycopg2',
        "NAME": env('NAME'),
        "USER": env('DBUSER'),
        "PASSWORD": env('PASSWORD'),
        "HOST": env('HOST'),
        "PORT": env('PORT')
    }
}
AUTH_USER_MODEL = 'accounts.CustomUser'


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# settings.py
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend
    'accounts.backends.EmailBackend',        # Your custom backend
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
DATETIME_FORMAT="%Y-%m-%d%H:%M:%S"
L10N=False
USE_TZ=False

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
# for static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


JWT_ENCODE_HANDLER = 'jwt_auth.utils.jwt_encode_handler'
JWT_DECODE_HANDLER = 'jwt_auth.utils.jwt_decode_handler',
JWT_PAYLOAD_HANDLER = 'jwt_auth.utils.jwt_payload_handler'
JWT_PAYLOAD_GET_USER_ID_HANDLER = 'jwt_auth.utils.jwt_get_user_id_from_payload_handler'
JWT_SECRET_KEY = env('SECRET_KEY')
JWT_ALGORITHM = 'HS256'
JWT_VERIFY = True
JWT_VERIFY_EXPIRATION = True
JWT_LEEWAY = 0
JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=300)
JWT_ALLOW_REFRESH = False
JWT_REFRESH_EXPIRATION_DELTA = datetime.timedelta(days=7)
JWT_AUTH_HEADER_PREFIX = 'Bearer'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp_host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'host_email@example.com'
EMAIL_HOST_PASSWORD = 'email_password'
DEFAULT_FROM_EMAIL = 'obedmeshachl@gmail.com'




# Add Celery configuration
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    
# setting up for cloudinary storage


# cloudinary.config(
#     cloud_name = env('CLOUDNAME'),
#     api_key = env('APIKEY'),
#     api_secret_key = env('CLOUDSECRET')
# )

MEDIA_URL = env('CLOUDINARY_URL')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': env('CLOUDNAME'),
#     'API_KEY': env('APIKEY'),
#     'API_SECRET': env('CLOUDSECRET'),
#     'ALLOWED_FORMATS': ('jpg', 'jpeg', 'png', 'gif', 'pdf'),
# }
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


