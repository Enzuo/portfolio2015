"""
WSGI config for myportfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os





os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myportfolio.settings")
#os.environ["DJANGO_SETTINGS_MODULE"] =  "myportfolio.settings"

#application = Cling(get_wsgi_application())

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
