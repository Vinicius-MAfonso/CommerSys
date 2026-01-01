from django.urls import path
from . import views

app_name = 'comercial'

urlpatterns = [
    path('contatos/', views.ContatoListView.as_view(), name='contatos'),
    path('contatos/novo/', views.ContatoCreateView.as_view(), name='contato_create'),
    path('contatos/<int:pk>/', views.ContatoDetailView.as_view(), name='contato_detail'),
    path('contatos/<int:pk>/editar/', views.ContatoUpdateView.as_view(), name='contato_edit'),
    path('contatos/<int:pk>/deletar/', views.ContatoDeleteView.as_view(), name='contato_delete'),
]