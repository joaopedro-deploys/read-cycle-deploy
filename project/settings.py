from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = (os.environ.get('DEBUG')) != 0

DEPLOY_HOST =  os.environ.get('WEB_HOSTNAME')

ALLOWED_HOSTS = [DEPLOY_HOST, "127.0.0.1", "read-cycle.azurewebsites.net"]

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000", f'https://{DEPLOY_HOST}.net', "https://read-cycle.azurewebsites.net/"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'book',
    'trade',
    'template_partials',
    'django_filters',

]
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT', 6379) #if ssl = true , port =6380
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"rediss://{REDIS_HOST}:{REDIS_PORT}/",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWORD
        }
    }
}


AUTHENTICATION_BACKENDS = [
    'main.backends.email_backend.EmailBackend',  
]


#AUTH_USER_MODEL = 'auth.User'
AUTH_USER_MODEL = 'main.UserModel'

LOGIN_URL = 'main:login-page'  
LOGIN_REDIRECT_URL = 'main:home-page'  
LOGOUT_REDIRECT_URL = 'main:login-page'  

AUTHENTICATION_BACKENDS = [
    'main.backends.email_backend.EmailBackend', 
    'django.contrib.auth.backends.ModelBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

ROOT_URLCONF = 'project.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base_templates' #content the main templates
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],                                                                      
        }
        },
        
]                           

WSGI_APPLICATION = 'project.wsgi.application'


# DATABASES = {
#     'default': dj_database_url.parse(os.environ.get('POSTGRES_PRODUCT_URL'))
# }

AZURE_POSTGRES_CONNECTION = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DBNAME'),
        'USER': os.environ.get('DBUSER'),
        'PASSWORD': os.environ.get('DBPASSWORD'),
        'HOST': os.environ.get('DBHOST'),
        'PORT': '5432'
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password   _validation.UserAttributeSimilarityValidator',
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True   

LOGOUT_REDIRECT_URL = '/login/'

STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    BASE_DIR / 'base_static'
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')



#default params app vars:
TRADE_STATUS_FLAGS = [
    ("OP", "Aberta"),
    ("AC", "Aceita"),
    ("FS", "Primeiro envio"),
    ("FN", "Finalizada" )
]

DATA_UPLOAD_MAX_MEMORY_SIZE = None

DATA_UPLOAD_MAX_NUMBER_FIELDS = None

NUMBER_PAGINATION_LIST = 12

DEFAULT_ANY_BOOK_PRICE = 100

DEFAULT_PX_WIDTH_BOOK_IMAGE = 128

DEFAULT_PX_HEIGTH_BOOK_IMAGE = 193

TIME_CACHE_LIST_VIEWS = 360  #in minutes