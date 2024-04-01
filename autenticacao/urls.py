from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('sair/', views.sair, name="sair")
    
]