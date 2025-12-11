from django.urls import path
from . import views

app_name = 'estoque_e_logistica'

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/create/', views.produtos_create, name='produtos_create'),
    path('produtos/update/<int:pk>/', views.produtos_update, name='produtos_update'),
    path('produtos/delete/<int:pk>/', views.produtos_delete, name='produtos_delete'),

    path('transportadoras/', views.transportadoras, name='transportadoras'),
    path('transportadoras/create/', views.transportadoras_create, name='transportadoras_create'),
    path('transportadoras/update/<int:pk>/', views.transportadoras_update, name='transportadoras_update'),
    path('transportadoras/delete/<int:pk>/', views.transportadoras_delete, name='transportadoras_delete'),
]