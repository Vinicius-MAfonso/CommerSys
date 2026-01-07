from django.urls import path
from . import views

app_name = 'comercial'

urlpatterns = [
    path('pedidos/', views.PedidoListView.as_view(), name='pedidos'),
    path('pedidos/novo/', views.PedidoCreateView.as_view(), name='pedido_create'),
    path('pedidos/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido_detail'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_edit'),
    path('clientes/<int:pk>/deletar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('contatos/', views.ContatoListView.as_view(), name='contatos'),
    path('contatos/novo/', views.ContatoCreateView.as_view(), name='contato_create'),
    path('contatos/<int:pk>/', views.ContatoDetailView.as_view(), name='contato_detail'),
    path('contatos/<int:pk>/editar/', views.ContatoUpdateView.as_view(), name='contato_edit'),
    path('contatos/<int:pk>/deletar/', views.ContatoDeleteView.as_view(), name='contato_delete'),
]