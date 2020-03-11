from django.urls import path

from usuarios.views import RegistrarUsuarioView
urlpatterns = [
        path(r'^registrar/$', RegistrarUsuarioView, name='registrar')
        
]