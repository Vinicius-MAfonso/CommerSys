from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('', views.pedido_list, name='pedido_list'),
    path('<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('create/', views.pedido_create, name='pedido_create'),
    path('<int:pk>/update/', views.pedido_update, name='pedido_update'),
    path('<int:pk>/delete/', views.pedido_delete, name='pedido_delete'),
]
