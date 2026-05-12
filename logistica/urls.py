from django.urls import path
from . import views

app_name = 'logistica'

urlpatterns = [
    # Produtos views
    path('produtos/', views.ProdutoListView.as_view(), name='produtos'),
    path('produtos/novo/', views.ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/', views.ProdutoDetailView.as_view(), name='produto_detail'),
    path('produtos/<int:pk>/editar/', views.ProdutoUpdateView.as_view(), name='produto_edit'),
    path('produtos/<int:pk>/deletar/', views.ProdutoDeleteView.as_view(), name='produto_delete'),
    
    # Transportadoras views
    path('transportadoras/', views.TransportadoraListView.as_view(), name='transportadoras'),
    path('transportadoras/novo/', views.TransportadoraCreateView.as_view(), name='transportadora_create'),
    path('transportadoras/<int:pk>/', views.TransportadoraDetailView.as_view(), name='transportadora_detail'),
    path('transportadoras/<int:pk>/editar/', views.TransportadoraUpdateView.as_view(), name='transportadora_edit'),
    path('transportadoras/<int:pk>/deletar/', views.TransportadoraDeleteView.as_view(), name='transportadora_delete'),
    
    # API endpoints
    path('api/produtos/', views.api_produtos_list, name='api_produtos_list'),
    path('api/produtos/<int:produto_id>/', views.api_produto_detail, name='api_produto_detail'),
]