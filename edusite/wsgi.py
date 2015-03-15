"""
WSGI config for edusite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys

# add project to path
sys.path.append('/home/zalewski/web_dev/edusite_project/edusite')

# add virtualenv site-packages to path
sys.path.append('/home/zalewski/.virtualenvs/edusite_project/lib/python3.3/site-packages')

os.environ["DJANGO_SETTINGS_MODULE"] = "edusite.settings.production"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
