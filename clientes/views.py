from django.shortcuts import render

def cliente_list(request):
    return render(request, 'clientes/clientes.html')

def cliente_detail(request, pk):
    pass
    # return render(request, 'clientes/cliente_detail.html')

def cliente_create(request):
    pass
    # return render(request, 'clientes/cliente_form.html')

def cliente_update(request, pk):
    pass
    # return render(request, 'clientes/cliente_form.html')

def cliente_delete(request, pk):
    pass
    # return render(request, 'clientes/cliente_confirm_delete.html')