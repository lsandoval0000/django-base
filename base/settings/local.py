from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y2_952mvx0w2@t#tr2-t42os77ry@(*h+sv-5)u3e#%6dnrl(v'

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'x'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'x'

# Twitter
SOCIAL_AUTH_TWITTER_KEY = 'x'
SOCIAL_AUTH_TWITTER_SECRET = 'x'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = 'x'
SOCIAL_AUTH_FACEBOOK_SECRET = 'x'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bd',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}