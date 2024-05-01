from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.urls import re_path
from django_eel.consumers import EelConsumer
from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "http": django_asgi_app([
        url(r"^eel$", EelConsumer.as_asgi()), # do not alter this line
    ]),

    "websocket": URLRouter([
        url(r"^eel$", EelConsumer.as_asgi()), # do not alter this line
    ]),
})