from django.urls import re_path 
from usuarios.views import RegistrarUsuarioView
urlpatterns = [
        
        re_path(r'^registrar/$', RegistrarUsuarioView.as_view(), name='registrar')

]