import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: don't run with debug turned on in production!

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'ckeditor',
    'sorl.thumbnail',
    'social_django',
    'phonenumber_field',
    'croppie',

    'users',
    'book',
    'club',
    'currency',
    'common',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middlewares.ClubSubDomainsMiddleware',
]

ROOT_URLCONF = 'bookgo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'autoescape': False,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookgo.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'users.User'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = 'media'

MEDIA_URL = '/media/'

# Social Config

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
    'users.pipeline.avatar',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '725388700117-tg1pvaqrfnlm136kvcg7s2tl63e66jir.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'gMoNDa0PJfTrh32UC0RMx9WK'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = []

SOCIAL_AUTH_FACEBOOK_KEY = '118993025389579'
SOCIAL_AUTH_FACEBOOK_SECRET = 'aeebc68a36c1dc4194a4b7dd2a00009d'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = 'TQFP2ZPb0CwMJPzCN96eDyfcj'
SOCIAL_AUTH_TWITTER_SECRET = 'sd4HfWaQtGtje9dvD8RaTJI5ngsMbcBJMqb4x4emVSSvJUJ2l1'

# Celery

CELERY_IMPORTS = (
    'book.tasks',
    'common.email',
)

# bookgo Settings

BOOK_CARD_IMAGE_WIDTH = 280
BOOK_CARD_IMAGE_HEIGHT = 380

BOOK_FULL_IMAGE_WIDTH = 450
BOOK_FULL_IMAGE_HEIGHT = 610

USER_AVATAR_WIDTH = 250
USER_AVATAR_HEIGHT = 250

BOOKS_TO_START_NEED = 40

USERS_NUM_TO_INVITE = 3

# Secret key only for a quick test
SECRET_KEY = '8#_ff2^xo@f=dvtgk&dhl9b0d5%ds3&g^$g&h_@tcx0!0mxq8s'
