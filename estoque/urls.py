from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/criar/', views.produto_create, name='produto_create'),
    path("produtos/<int:pk>/detalhes/", views.produto_detail, name="produto_detail"),
    path('produtos/<int:pk>/editar/', views.produto_update, name='produto_update'),
    path('produtos/<int:pk>/deletar/', views.produto_delete, name='produto_delete'),
    path('transportadoras/', views.transportadoras, name='transportadoras'),
    path('transportadoras/criar/', views.transportadora_create, name='transportadora_create'),
    path('transportadoras/<int:pk>/detalhes/', views.transportadora_detail, name='transportadora_detail'),
    path('transportadoras/<int:pk>/editar/', views.transportadora_update, name='transportadora_update'),
    path('transportadoras/<int:pk>/deletar/', views.transportadora_delete, name='transportadora_delete'),
]