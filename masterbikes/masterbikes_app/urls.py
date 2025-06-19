from django.urls import path
from .views import login, registro, recuperar_contraseña, usuario_creado, inicio

urlpatterns = [
    path('login/', login, name='login'),
    path('registro', registro, name='registro'),
    path('recuperar_contrasena', recuperar_contraseña, name='recuperar_contraseña'), 
    path('usuario_creado', usuario_creado, name='usuario_creado'),
    path('', inicio, name='incio'),
]
