import dj_database_url
import django_heroku
import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['.herokuapp.com']

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ['x']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ['x']

# Twitter
SOCIAL_AUTH_TWITTER_KEY = os.environ['x']
SOCIAL_AUTH_TWITTER_SECRET = os.environ['x']

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = os.environ['x']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['x']

# Database
DATABASES = {'default': dj_database_url.config()}

django_heroku.settings(locals())