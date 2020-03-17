from django.urls import path 
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views as auth_views
from django.contrib.auth import views

urlpatterns = [
        path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
        path('login/', auth_views.LoginView.as_view(template_name="Login.html"), name="login"),
        path('logout/', views.logout_then_login, {'login_url': '/login/'}, name='logout')

]
