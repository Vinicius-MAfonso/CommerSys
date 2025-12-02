from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('<int:pk>/', views.produto_detail, name='produto_detail'),
    path('create/', views.produto_create, name='produto_create'),
    path('<int:pk>/update/', views.produto_update, name='produto_update'),
    path('<int:pk>/delete/', views.produto_delete, name='produto_delete'),
]
