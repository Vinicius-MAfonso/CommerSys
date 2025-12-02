from django.shortcuts import render

def pedido_list(request):
    return render(request, 'pedidos/pedidos.html')
def pedido_detail(request, pk):
    pass
def pedido_create(request):
    pass
def pedido_update(request, pk):
    pass
def pedido_delete(request, pk):
    pass