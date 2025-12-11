from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto, Transportadora


def produtos(request):
    try:
        produtos = Produto.objects.all()
    except Exception:
        messages.error(request, f"Erro ao carregar produtos!")
        produtos = []
    return render(request, "produtos/produtos.html", {"produtos": produtos})


def detalhes_produto(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
    except Produto.DoesNotExist:
        messages.error(request, "Produto não encontrado!")
        return redirect("estoque:produtos")
    except Exception:
        messages.error(request, f"Erro ao carregar o produto!")
        return redirect("estoque:produtos")
    return render(request, "produtos/detalhes_produto.html", {"produto": produto})


def criar_produto(request):
    try:
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco") or None
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco)
    except Exception:
        messages.error(request, f"Erro ao criar o produto!")
        return redirect("estoque:produtos")
    messages.success(request, "Produto criado com sucesso!")
    return redirect("estoque:produtos")


def editar_produto(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.nome = request.POST.get("nome")
        produto.descricao = request.POST.get("descricao")
        produto.preco = request.POST.get("preco") or None
        produto.save()
    except Produto.DoesNotExist:
        messages.error(request, "Produto não encontrado!")
        return redirect("estoque:produtos")
    except Exception:
        messages.error(request, f"Erro ao atualizar o produto!")
        return redirect("estoque:produtos")
    messages.success(request, "Produto atualizado com sucesso!")
    return redirect("estoque:produtos")


def deletar_produto(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
    except Produto.DoesNotExist:
        messages.error(request, "Produto não encontrado!")
        return redirect("estoque:produtos")
    except Exception:
        messages.error(request, f"Erro ao deletar o produto!")
        return redirect("estoque:produtos")
    messages.success(request, "Produto deletado com sucesso!")
    return redirect("estoque:produtos")


def transportadoras(request):
    try:
        transportadoras = Transportadora.objects.all()
    except Exception:
        messages.error(request, f"Erro ao carregar transportadoras!")
        transportadoras = []
    return render(
        request,
        "transportadoras/transportadoras.html",
        {"transportadoras": transportadoras},
    )


def detalhes_transportadora(request, pk):
    try:
        transportadora = Transportadora.objects.get(pk=pk)
    except Transportadora.DoesNotExist:
        messages.error(request, "Transportadora não encontrada!")
        return redirect("estoque:transportadoras")
    except Exception:
        messages.error(request, f"Erro ao carregar a transportadora!")
        return redirect("estoque:transportadoras")
    return render(
        request,
        "transportadoras/detalhes_transportadora.html",
        {"transportadora": transportadora},
    )


def criar_transportadora(request):
    try:
        nome = request.POST.get("nome")
        Transportadora.objects.create(nome=nome)
    except Exception:
        messages.error(request, f"Erro ao criar a transportadora!")
        return redirect("estoque:transportadoras")
    messages.success(request, "Transportadora criada com sucesso!")
    return redirect("estoque:transportadoras")


def editar_transportadora(request, pk):
    try:
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.nome = request.POST.get("nome")
        transportadora.save()
    except Transportadora.DoesNotExist:
        messages.error(request, "Transportadora não encontrada!")
        return redirect("estoque:transportadoras")
    except Exception:
        messages.error(request, f"Erro ao atualizar a transportadora!")
        return redirect("estoque:transportadoras")
    messages.success(request, "Transportadora atualizada com sucesso!")
    return redirect("estoque:transportadoras")


def deletar_transportadora(request, pk):
    try:
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.delete()
    except Transportadora.DoesNotExist:
        messages.error(request, "Transportadora não encontrada.")
        return redirect("estoque:transportadoras")
    except Exception:
        messages.error(request, f"Erro ao deletar a transportadora!")
        return redirect("estoque:transportadoras")
    messages.success(request, "Transportadora deletada com sucesso!")
    return redirect("estoque:transportadoras")
