# biblioteca_project/urls.py

from django.contrib import admin
from django.urls import path, include
from libros.jwt_views import CustomTokenObtainPairView
from libros import web_views  # ← AGREGAR


urlpatterns = [
    # JWT personalizado
    path('auth/jwt/login/', CustomTokenObtainPairView.as_view(), name='jwt_login'),
    # Admin de Django
    path('admin/', admin.site.urls),
    
    # ✨ URLs de la API (AGREGAR ESTA LÍNEA)
    path('api/', include('libros.api_urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('', web_views.home, name='home'),
    path('oauth/login/', web_views.oauth_login, name='oauth_login'),
    path('login/jwt/', web_views.jwt_login_page, name='jwt_login_page'),
]