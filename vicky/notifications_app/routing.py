#Same like urls.py for http/wsgi server

from django.urls import path
from .consumers import NotificationsConsumer

ws_urlpatterns=[
    path('ws/notifications/', NotificationsConsumer.as_asgi()),
]