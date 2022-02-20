import logging.config
import os

from pathlib import Path
from envparse import env


BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_file = os.path.join(BASE_DIR.parent, "project_config/.env.config")

if os.path.isfile(dotenv_file):
    env.read_envfile(dotenv_file)

# Базовые настройки приложения
SECRET_KEY = env.str("SECRET_KEY")

DATA_UPLOAD_MAX_NUMBER_FIELDS = env.int("DATA_UPLOAD_MAX_NUMBER_FIELDS")

SECURE_PROXY_SSL_HEADER = env.tuple("SECURE_PROXY_SSL_HEADER")

DEBUG = env.bool("DEBUG")

PRODUCTION = env.bool("PRODUCTION")

ROOT_URLCONF = "config.urls"

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

# Настройки языка и времени
LANGUAGE_CODE = env.str("LANGUAGE_CODE")

TIME_ZONE = env.str("TIME_ZONE")

USE_I18N = env.bool("USE_I18N")

USE_L10N = env.bool("USE_L10N")

USE_TZ = env.bool("USE_TZ")

# Базовые настройки базы данных
DB_USER = env.str("DB_USER")

DB_USER_PASSWORD = env.str("DB_USER_PASSWORD")

DB_HOST = env.str("DB_HOST")

DB_NAME = env.str("DB_NAME")

DB_PORT = env.str("DB_PORT")

CONN_MAX_AGE = env.int("CONN_MAX_AGE")

# Настройки CORS
CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS")

CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS")

CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST")

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS")

# Базовые настройки Celery
RABBITMQ_DEFAULT_USER = env.str("RABBITMQ_DEFAULT_USER")

RABBITMQ_DEFAULT_PASS = env.str("RABBITMQ_DEFAULT_PASS")

CELERY_BROKER_URL = f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@rabbit:5672/"

CELERY_ACCEPT_CONTENT = env.list("CELERY_ACCEPT_CONTENT")

CELERY_TASK_SERIALIZER = env.str("CELERY_TASK_SERIALIZER")

CELERY_RESULT_SERIALIZER = env.str("CELERY_RESULT_SERIALIZER")

CELERYD_PREFETCH_MULTIPLIER = env.int("CELERYD_PREFETCH_MULTIPLIER")

CELERY_TIMEZONE = env.str("CELERY_TIMEZONE")

CELERY_CACHE_BACKEND = env.str("CELERY_CACHE_BACKEND")

CELERY_RESULT_BACKEND = env.str("CELERY_RESULT_BACKEND")

CELERY_CREATE_MISSING_QUEUES = env.bool("CELERY_CREATE_MISSING_QUEUES")

CELERYD_MAX_TASKS_PER_CHILD = env.int("CELERYD_MAX_TASKS_PER_CHILD")

CELERY_BROKER_CONNECTION_RETRY = env.bool("CELERY_BROKER_CONNECTION_RETRY")

CELERY_DISABLE_RATE_LIMITS = env.bool("CELERY_DISABLE_RATE_LIMITS")

CELERY_BROKER_CONNECTION_MAX_RETRIES = env.int("CELERY_BROKER_CONNECTION_MAX_RETRIES")

# Установленные приложения
INSTALLED_APPS = [
    # Defaults
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Api
    "rest_framework",
    # Celery
    'django_celery_results',
    'djcelery_email',
    # Own apps
    "comparator",
    # CORS
    "whitenoise.runserver_nostatic",
    "corsheaders",
]

# Промежуточные слои
MIDDLEWARE = [
    # Defaults
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

# Настройка шаблонизатора
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            'loaders': [
                # Loads templates from admin_tools setting:
                "admin_tools.template_loaders.Loader",
                # Loads templates from DIRS setting:
                "django.template.loaders.filesystem.Loader",
                # Loads templates from your installed apps:
                "django.template.loaders.app_directories.Loader",
            ],

        },
    },
]

# Настройка запуска приложения
ASGI_APPLICATION = "config.asgi.application"

# Настройка базы данных
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_USER_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}

# Настройки кэша
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'local_caching',
    },
    'snowflake': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'TIMEOUT': 5 * 60,  # 5*60 = 5 minutes
    },
    'longhorn': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
        'TIMEOUT': 1 * 60 * 60,  # 1*60*60 = 1 hour
    },
}

# Модель пользователя
AUTH_USER_MODEL = "users.User"

# Путь к статическим файлам
STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "documentation")
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Настройки DRF
REST_FRAMEWORK = {
    # Права доступа поумолчанию
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ],
    # Тип токенов и авторизации
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication"
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "url_filter.integrations.drf.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}

# Логгироваине
LOGGING_CONFIG = None

LOGLEVEL = env.str("DJANGO_LOGLEVEL").upper()

logging.config.dictConfig = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
                '%(asctime)s [%(levelname)s] %(ip)s %(email)s '
                '%(pathname)s:%(lineno)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', ],
            'level': LOGLEVEL,
            'propagate': True,
        },
    }
}
