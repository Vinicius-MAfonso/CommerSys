from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/produtos.html', {'produtos': produtos})
def produto_create(request):
    try:
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        preco = request.POST.get('preco') or None
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco)
    except Exception as e:
        messages.error(request, f'Erro ao criar o produto: {str(e)}')
        return redirect('produtos:produto_list')
    messages.success(request, 'Produto criado com sucesso!')
    return redirect('produtos:produto_list')
def produto_update(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.nome = request.POST.get('nome')
        produto.descricao = request.POST.get('descricao')
        produto.preco = request.POST.get('preco') or None
        produto.save()
    except Produto.DoesNotExist:
        messages.error(request, 'Produto não encontrado.')
        return redirect('produtos:produto_list')
    except Exception as e:
        messages.error(request, f'Erro ao atualizar o produto: {str(e)}')
        return redirect('produtos:produto_list')
    messages.success(request, 'Produto atualizado com sucesso!')
    return redirect('produtos:produto_list')

def produto_delete(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
    except Produto.DoesNotExist:
        messages.error(request, 'Produto não encontrado.')
        return redirect('produtos:produto_list')
    except Exception as e:
        messages.error(request, f'Erro ao deletar o produto: {str(e)}')
        return redirect('produtos:produto_list')
    messages.success(request, 'Produto deletado com sucesso!')
    return redirect('produtos:produto_list')