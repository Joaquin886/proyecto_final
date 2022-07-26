from django.urls import path
from django.contrib.auth.views import LogoutView
from Core import views

urlpatterns = [
    path('super_user_registro/', views.super_user_registro, name = 'super_user_registro'),
    path('usuario_registro/', views.usuario_registro, name = 'usuario_registro'),
    path('super_user_login/', views.super_user_login, name = 'super_user_login'),
    path('usuario_login', views.usuario_login, name = 'usuario_login'),
    path('logout', LogoutView.as_view(template_name='Core/logout.html'), name='logout'),
]