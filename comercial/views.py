from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente, Produto

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})
def clientes_create(request):
    try:
        nome_razao_social = request.POST.get('nome_razao_social')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        telefone_principal = request.POST.get('telefone_principal')
        endereco = request.POST.get('endereco')
        inscricao_estadual = request.POST.get('inscricao_estadual')
        Cliente.objects.create(nome_razao_social=nome_razao_social, cpf_cnpj=cpf_cnpj, telefone_principal=telefone_principal, endereco=endereco, inscricao_estadual=inscricao_estadual)
    except Exception as e:
        messages.error(request, f"Erro ao criar cliente: {e}")
        return redirect('comercial:clientes')
    messages.success(request, "Cliente criado com sucesso.")
    return redirect('comercial:clientes')

def clientes_update(request, pk):
    pass
    # return render(request, 'comercial/cliente_form.html')

def clientes_delete(request, pk):
    pass
    # return render(request, 'comercial/cliente_confirm_delete.html')


def contatos(request):
    pass
def contatos_create(request):
    pass
def contatos_update(request, pk):
    pass
def contatos_delete(request, pk):
    pass

def pedidos(request):
    pass
def pedidos_create(request):
    pass
def pedidos_update(request, pk):
    pass
def pedidos_delete(request, pk):
    pass
