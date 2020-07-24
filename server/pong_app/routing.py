from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("<game>/", consumers.PongConsumer),
]
