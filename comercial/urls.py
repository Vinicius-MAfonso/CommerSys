from django.urls import path
from . import views

app_name = 'comercial'

urlpatterns = [
    path("clientes/", views.clientes, name="clientes"),
    path("clientes/criar/", views.cliente_create, name="cliente_create"),
    path("clientes/<int:pk>/detalhes/", views.cliente_detail, name="cliente_detail"),
    path("clientes/<int:pk>/editar/", views.cliente_update, name="cliente_update"),
    path("clientes/<int:pk>/deletar/", views.cliente_delete, name="cliente_delete"),
]