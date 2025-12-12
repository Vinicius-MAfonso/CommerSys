from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente, Produto

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})
def criar_cliente(request):
    try:
        nome_razao_social = request.POST.get('nome_razao_social')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        telefone_principal = request.POST.get('telefone_principal')
        endereco = request.POST.get('endereco')
        inscricao_estadual = request.POST.get('inscricao_estadual')
        Cliente.objects.create(nome_razao_social=nome_razao_social, cpf_cnpj=cpf_cnpj, telefone_principal=telefone_principal, endereco=endereco, inscricao_estadual=inscricao_estadual)
    except Exception:
        messages.error(request, f"Erro ao criar cliente!")
    except Exception:
        messages.error(request, f"Erro ao criar cliente!")
        return redirect('comercial:clientes')
    messages.success(request, "Cliente criado com sucesso!")
    messages.success(request, "Cliente criado com sucesso!")
    return redirect('comercial:clientes')

def clientes_update(request, pk):
    pass

def clientes_delete(request, pk):
    pass


def contatos(request):
    pass
def contato_criar(request):
    pass
def contato_update(request, pk):
    pass
def contato_delete(request, pk):
    pass

def pedidos(request):
    pass
def pedido_criar(request):
    pass
def pedido_update(request, pk):
    pass
def pedido_delete(request, pk):
    pass
