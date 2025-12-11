from django.urls import path
from . import views

app_name = 'comercial'

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/criar/', views.criar_cliente, name='criar_cliente'),
    path('clientes/update/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('clientes/delete/<int:pk>/', views.deletar_cliente, name='deletar_cliente'),

    path('contatos/', views.contatos, name='contatos'),
    path('contatos/criar/', views.contato_criar, name='contato_criar'),
    path('contatos/update/<int:pk>/', views.contato_update, name='contato_update'),
    path('contatos/delete/<int:pk>/', views.contato_delete, name='contato_delete'),

    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/criar/', views.pedido_criar, name='pedido_criar'),
    path('pedidos/update/<int:pk>/', views.pedido_update, name='pedido_update'),
    path('pedidos/delete/<int:pk>/', views.pedido_delete, name='pedido_delete'),
]