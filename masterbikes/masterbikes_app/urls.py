from django.urls import path
from .views import login, registro

urlpatterns = [
    path('*', login, name='login'),
    path('login', login, name='login'),
    path('registro', registro, name='registro'),
]
