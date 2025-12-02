from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('create/', views.cliente_create, name='cliente_create'),
    path('<int:pk>/update/', views.cliente_update, name='cliente_update'),
    path('<int:pk>/delete/', views.cliente_delete, name='cliente_delete'),
]