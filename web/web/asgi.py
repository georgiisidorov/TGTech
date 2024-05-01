"""
ASGI config for web project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import re_path
from django_eel.consumers import EelConsumer
from django.core.asgi import get_asgi_application
# from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.web.settings')
os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})

# django_asgi_app = get_asgi_application()

django.setup()

application = get_asgi_application()
# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     "http": django_asgi_app([
#         url(r"^eel$", EelConsumer.as_asgi()), # do not alter this line
#     ]),

#     "websocket": URLRouter([
#         url(r"^eel$", EelConsumer.as_asgi()), # do not alter this line
#     ]),
# })