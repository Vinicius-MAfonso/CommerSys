from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto, Transportadora

def produtos(request):
    try:
        produtos = Produto.objects.all()
    except Exception as e:
        messages.error(request, f'Erro ao carregar produtos: {str(e)}')
        produtos = []
    return render(request, 'produtos/produtos.html', {'produtos': produtos})
def produtos_create(request):
    try:
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco') or None
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco)
    except Exception as e:
        messages.error(request, f'Erro ao criar o produto: {str(e)}')
        return redirect('estoque_e_logistica:produtos')
    messages.success(request, 'Produto criado com sucesso!')
    return redirect('estoque_e_logistica:produtos')
def produtos_update(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco') or None
        produto.save()
    except Produto.DoesNotExist:
        messages.error(request, 'Produto não encontrado.')
        return redirect('estoque_e_logistica:produtos')
    except Exception as e:
        messages.error(request, f'Erro ao atualizar o produto: {str(e)}')
        return redirect('estoque_e_logistica:produtos')
    messages.success(request, 'Produto atualizado com sucesso!')
    return redirect('estoque_e_logistica:produtos')

def produtos_delete(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
    except Produto.DoesNotExist:
        messages.error(request, 'Produto não encontrado.')
        return redirect('estoque_e_logistica:produtos')
    except Exception as e:
        messages.error(request, f'Erro ao deletar o produto: {str(e)}')
        return redirect('estoque_e_logistica:produtos')
    messages.success(request, 'Produto deletado com sucesso!')
    return redirect('estoque_e_logistica:produtos')

def transportadoras(request):
    try:
        transportadoras = Transportadora.objects.all()
    except Exception as e:
        messages.error(request, f'Erro ao carregar transportadoras: {str(e)}')
        transportadoras = []
    return render(request, 'transportadoras/transportadoras.html', {'transportadoras': transportadoras})
def transportadoras_create(request):
    try:
        nome = request.POST.get('nome')
        Transportadora.objects.create(nome=nome)
    except Exception as e:
        messages.error(request, f'Erro ao criar a transportadora: {str(e)}')
        return redirect('estoque_e_logistica:transportadoras')
    messages.success(request, 'Transportadora criada com sucesso!')
    return redirect('estoque_e_logistica:transportadoras')
def transportadoras_update(request, pk):
    try:
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.nome = request.POST.get('nome')
        transportadora.save()
    except Transportadora.DoesNotExist:
        messages.error(request, 'Transportadora não encontrada.')
        return redirect('estoque_e_logistica:transportadoras')
    except Exception as e:
        messages.error(request, f'Erro ao atualizar a transportadora: {str(e)}')
        return redirect('estoque_e_logistica:transportadoras')
    messages.success(request, 'Transportadora atualizada com sucesso!')
    return redirect('estoque_e_logistica:transportadoras')
def transportadoras_delete(request, pk):
    try:
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.delete()
    except Transportadora.DoesNotExist:
        messages.error(request, 'Transportadora não encontrada.')
        return redirect('estoque_e_logistica:transportadoras')
    except Exception as e:
        messages.error(request, f'Erro ao deletar a transportadora: {str(e)}')
        return redirect('estoque_e_logistica:transportadoras')
    messages.success(request, 'Transportadora deletada com sucesso!')
    return redirect('estoque_e_logistica:transportadoras')