"""
ASGI config for chatsystemproj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatsystemproj.settings')

from chatapp.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})


# The asgi.py file serves the entry point for asynchronous communication, enabling Django to handle WebSocket connections via the ASGI interface.
# The django channels checks at the type of connection (the ProtocolTypeRouter) whether it's an http or ws connection
# If it's a ws connection, it will be given to the AuthMiddlewareStack class to identify the user like django does with its auth model
# After that, the connection will be given to the URLRouter class that passes it to the consumer that was defined in the websocket_urlpatterns list


# An instance of the AuthMiddlewareStack will be initiatedand.
# As for the argument, the AuthMiddlewareStack has an instance of the URLRouter class and pass websocket_urlpatterns (which is defined in the routing.py) as an argument to the URLRouter class.