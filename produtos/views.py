from django.shortcuts import render

def produto_list(request):
    return render(request, 'produtos/produtos.html')
def produto_detail(request, pk):
    pass
def produto_create(request):
    pass
def produto_update(request, pk):
    pass
def produto_delete(request, pk):
    pass