from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # Notificaciones no usa parámetros, se queda igual
    re_path(r'ws/notificaciones/$', consumers.NotificacionesConsumer.as_asgi()),
    
    # CORRECCIÓN: Se agrega <room_name> y la barra invertida doble o r'' para \w
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]