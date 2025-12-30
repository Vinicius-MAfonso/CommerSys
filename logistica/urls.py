from django.urls import path
from . import views

app_name = 'logistica'

urlpatterns = [
    path('produtos/', views.ProdutoListView.as_view(), name='produtos'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_edit'),
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    path('transportadoras/', views.TransportadoraListView.as_view(), name='transportadoras'),
    path('transportadoras/novo/', views.TransportadoraCreateView.as_view(), name='transportadora_create'),
    path('transportadoras/<int:pk>/', views.TransportadoraDetailView.as_view(), name='transportadora_detail'),
    path('transportadoras/<int:pk>/editar/', views.TransportadoraUpdateView.as_view(), name='transportadora_edit'),
    path('transportadoras/<int:pk>/deletar/', views.TransportadoraDeleteView.as_view(), name='transportadora_delete'),
]