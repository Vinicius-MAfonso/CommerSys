from django.urls import path
from . import views

app_name = 'comercial'

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/create/', views.clientes_create, name='clientes_create'),
    path('clientes/update/<int:pk>/', views.clientes_update, name='clientes_update'),
    path('clientes/delete/<int:pk>/', views.clientes_delete, name='clientes_delete'),

    path('contatos/', views.contatos, name='contatos'),
    path('contatos/create/', views.contatos_create, name='contatos_create'),
    path('contatos/update/<int:pk>/', views.contatos_update, name='contatos_update'),
    path('contatos/delete/<int:pk>/', views.contatos_delete, name='contatos_delete'),

    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/create/', views.pedidos_create, name='pedidos_create'),
    path('pedidos/update/<int:pk>/', views.pedidos_update, name='pedidos_update'),
    path('pedidos/delete/<int:pk>/', views.pedidos_delete, name='pedidos_delete'),
]