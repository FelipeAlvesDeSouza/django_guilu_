from django.contrib import admin
from django.urls import path , re_path
from perfis import views


urlpatterns = [
    path('' , views.index , name = 'index'),
    re_path(r'^perfis/(?P<perfil_id>\d+)$', views.exibir , name = 'exibir'),
    re_path(r'^perfis/(?P<perfil_id>\d+)/convidar$' , views.convidar , name= 'convidar'),
    re_path(r'^perfis/(?P<convite_id>\d+)/aceitar$' , views.aceitar , name= 'aceitar'),
    
]
