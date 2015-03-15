# settings/production.py

from .local import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = '/home/zalewski/public_html/media'
MEDIA_URL = '/~zalewski/media/'
STATIC_URL = '/~zalewski/static/'
