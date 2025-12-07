from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('<int:pk>/', views.produto_edit, name='produto_edit'),
    path('create/', views.produto_create, name='produto_create'),
    path('update/<int:pk>/', views.produto_update, name='produto_update'),
    path('delete/<int:pk>/', views.produto_delete, name='produto_delete'),
]
