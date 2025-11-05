from pathlib import Path
import os
import dotenv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

render_secret_path = Path('/etc/secrets/.env.prod')

if render_secret_path.exists():
    dotenv.load_dotenv(render_secret_path)
    os.environ.setdefault('ENVIRONMENT', 'production')

else:
    dotenv_path = BASE_DIR / '.env.local'
    if dotenv_path.exists():
        dotenv.load_dotenv(dotenv_path)


ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')


SECRET_KEY = os.getenv('SECRET_KEY')

# O padrão é 'False' por segurança
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Carrega do .env e divide a string por vírgulas
ALLOWED_HOSTS_STR = os.getenv('ALLOWED_HOSTS')
ALLOWED_HOSTS = ALLOWED_HOSTS_STR.split(',') if ALLOWED_HOSTS_STR else []


INSTALLED_APPS = [
    'accounts',
    'core',
    'clientes',
    'produtos',
    'pedidos',
    'anymail',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "no-reply@commersys.local")

EMAIL_BACKEND = "anymail.backends.brevo.EmailBackend"

ANYMAIL = {
    "BREVO_API_KEY": os.getenv("BREVO_API_KEY"),
}

ROOT_URLCONF = 'commersys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'commersys.wsgi.application'


DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', f'sqlite:///{BASE_DIR / "db.sqlite3"}')
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]



LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
LOGIN_URL = '/accounts/login/'

try:
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.SUCCESS: 'bg-success',
        messages.DEBUG: 'bg-info text-dark',
        messages.INFO: 'bg-info text-dark',
        messages.WARNING: 'bg-warning text-dark',
        messages.ERROR: 'bg-danger',
    }
except Exception as e:
    pass