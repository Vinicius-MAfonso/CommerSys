from django.urls import path
from . import views

app_name = 'estoque'

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path("produtos/detail/<int:pk>/", views.produto_detail, name="produto_detail"),
    path('produtos/create/', views.produto_create, name='produto_create'),
    path('produtos/update/<int:pk>/', views.produto_update, name='produto_update'),
    path('produtos/delete/<int:pk>/', views.produto_delete, name='produto_delete'),
    path('transportadoras/', views.transportadoras, name='transportadoras'),
    path('transportadoras/detail/<int:pk>/', views.transportadora_detail, name='transportadora_detail'),
    path('transportadoras/create/', views.transportadora_create, name='transportadora_create'),
    path('transportadoras/update/<int:pk>/', views.transportadora_update, name='transportadora_update'),
    path('transportadoras/delete/<int:pk>/', views.transportadora_delete, name='transportadora_delete'),
]