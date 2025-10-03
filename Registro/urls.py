from django.contrib import admin
from django.urls import path, include
from .views import registrar_usuario
urlpatterns = [
    path('', registrar_usuario, name='registro'),
]
