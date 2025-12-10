from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('create/', views.cliente_create, name='cliente_create'),
    path('update/<int:pk>', views.cliente_update, name='cliente_update'),
    path('delete/<int:pk>', views.cliente_delete, name='cliente_delete'),
]