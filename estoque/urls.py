from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/criar/', views.criar_produto, name='criar_produto'),
    path('produtos/<int:pk>/detail/', views.detalhes_produto, name='detalhes_produto'),
    path('produtos/<int:pk>/update/', views.editar_produto, name='editar_produto'),
    path('produtos/<int:pk>/delete/', views.deletar_produto, name='deletar_produto'),

    path('transportadoras/', views.transportadoras, name='transportadoras'),
    path('transportadoras/criar/', views.criar_transportadora, name='criar_transportadora'),
    path('transportadoras/<int:pk>/detail/', views.detalhes_transportadora, name='detalhes_transportadora'),
    path('transportadoras/<int:pk>/update/', views.editar_transportadora, name='editar_transportadora'),
    path('transportadoras/<int:pk>/delete/', views.deletar_transportadora, name='deletar_transportadora'),
]