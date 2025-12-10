from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cliente

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})
def cliente_create(request):
    try:
        nome_razao_social = request.POST.get('nome_razao_social')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        telefone_principal = request.POST.get('telefone_principal')
        endereco = request.POST.get('endereco')
        inscricao_estadual = request.POST.get('inscricao_estadual')
        Cliente.objects.create(nome_razao_social=nome_razao_social, cpf_cnpj=cpf_cnpj, telefone_principal=telefone_principal, endereco=endereco, inscricao_estadual=inscricao_estadual)
    except Exception as e:
        messages.error(request, f"Erro ao criar cliente: {e}")
        return redirect('clientes:cliente_list')
    messages.success(request, "Cliente criado com sucesso.")
    return redirect('clientes:cliente_list')

def cliente_update(request, pk):
    pass
    # return render(request, 'clientes/cliente_form.html')

def cliente_delete(request, pk):
    pass
    # return render(request, 'clientes/cliente_confirm_delete.html')