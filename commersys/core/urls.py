from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('produtos/', views.produtos, name='produtos'),
    path('clientes/', views.clientes, name='clientes'),
]
