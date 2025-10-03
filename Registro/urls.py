from django.contrib import admin
from django.urls import path, include
from .views import registrar_usuario
from .views import registrar_usuario_tienda
urlpatterns = [
    path('', registrar_usuario, name='registro'),
    path('tienda/', registrar_usuario_tienda, name='registro_tienda'),
]
