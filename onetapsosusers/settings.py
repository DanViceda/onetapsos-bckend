from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-jbilu%!qfp0@$1s2m=fz%u)aha3l)x$gi&6jj3sv(_@hz*-j9a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Hosts allowed to access the server (use '*' for development, restrict in production)
# settings.py
ALLOWED_HOSTS = [
    "127.0.0.1",  # local testing
    "localhost",
    "onetapsos-bckend.onrender.com",  # Render URL
]



# For development only

# Installed apps (core Django + custom + third-party)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom app
    'users',

    # Third-party apps
    'rest_framework',
    'corsheaders',
]

# Middleware stack (request/response processing)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Must be above CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

# Root URL configuration
ROOT_URLCONF = 'onetapsosusers.urls'

# Template engine configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'users' / 'templates'],
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

# WSGI application entry point
WSGI_APPLICATION = 'onetapsosusers.wsgi.application'

# Database configuration (SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # SQLite database file
    }
}


# Password validation rules
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

# Internationalization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'  # Adjusted for your location
USE_I18N = True
USE_TZ = True

# Static file configuration
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model reference
AUTH_USER_MODEL = 'users.CustomUser'

# CORS configuration (allow all origins for development)
CORS_ALLOW_ALL_ORIGINS = True

# Optional: REST Framework global settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
