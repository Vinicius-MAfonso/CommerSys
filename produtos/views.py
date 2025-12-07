from django.shortcuts import render
from .models import Produto

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})
def produto_edit(request, pk):
    pass
def produto_create(request):
    pass
def produto_update(request, pk):
    pass
def produto_delete(request, pk):
    pass