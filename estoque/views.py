from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Produto, Transportadora
import logging


logger = logging.getLogger(__name__)

def produtos(request):
    try:
        produtos = Produto.objects.all()
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao carregar produtos!")
        produtos = []
    return render(request, "produtos/produtos.html", {"produtos": produtos})


def produto_detail(request, pk):
    if request.method == "GET":
        try:
            produto = Produto.objects.get(pk=pk)
            data = {
                "id": produto.id,
                "nome": produto.nome,
                "descricao": produto.descricao,
                "preco": produto.preco,
            }
            return JsonResponse(data)
        except Produto.DoesNotExist:
            return JsonResponse({"error": "Produto não encontrado."}, status=404)
        except Exception as e:
            logger.exception(e)
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método não permitido."}, status=405)

def produto_create(request):
    try:
        nome = request.POST.get("nome")
        descricao = request.POST.get("descricao")
        preco = request.POST.get("preco") or None
        Produto.objects.create(nome=nome, descricao=descricao, preco=preco)
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao criar o produto!")
        return redirect("estoque:produtos")
    messages.success(request, "Produto criado com sucesso!")
    return redirect("estoque:produtos")


def produto_update(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.nome = request.POST.get("nome")
        produto.descricao = request.POST.get("descricao")
        produto.preco = request.POST.get("preco") or None
        produto.save()
    except Produto.DoesNotExist:
        messages.error(request, "Produto não encontrado.")
        return redirect("estoque:produtos")
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao atualizar o produto!")
        return redirect("estoque:produtos")
    messages.success(request, "Produto atualizado com sucesso!")
    return redirect("estoque:produtos")


def produto_delete(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
        produto.delete()
    except Produto.DoesNotExist:
        messages.error(request, "Produto não encontrado.")
        return redirect("estoque:produtos")
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao deletar o produto!")
        return redirect("estoque:produtos")
    messages.success(request, "Produto deletado com sucesso!")
    return redirect("estoque:produtos")


def transportadoras(request):
    try:
        transportadoras = Transportadora.objects.all()
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao carregar transportadoras!")
        transportadoras = []
    return render(
        request,
        "transportadoras/transportadoras.html",
        {"transportadoras": transportadoras},
    )

def transportadora_detail(request, pk):
    if request.method == "GET":
        try:
            transportadora = Transportadora.objects.get(pk=pk)
            data = {
                "id": transportadora.id,
                "nome": transportadora.nome,
            }
            return JsonResponse(data)
        except Transportadora.DoesNotExist:
            return JsonResponse({"error": "Transportadora não encontrada."}, status=404)
        except Exception as e:
            logger.exception(e)
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método não permitido."}, status=405)

def transportadora_create(request):
    try:
        nome = request.POST.get("nome")
        Transportadora.objects.create(nome=nome)
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao criar a transportadora!")
        return redirect("estoque:transportadoras")
    messages.success(request, "Transportadora criada com sucesso!")
    return redirect("estoque:transportadoras")


def transportadora_update(request, pk):
    try:
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.nome = request.POST.get("nome")
        transportadora.save()
    except Transportadora.DoesNotExist:
        messages.error(request, "Transportadora não encontrada.")
        return redirect("estoque:transportadoras")
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao atualizar a transportadora!")
        return redirect("estoque:transportadoras")
    messages.success(request, "Transportadora atualizada com sucesso!")
    return redirect("estoque:transportadoras")


def transportadora_delete(request, pk):
    try:
        transportadora = Transportadora.objects.get(pk=pk)
        transportadora.delete()
    except Transportadora.DoesNotExist:
        messages.error(request, "Transportadora não encontrada.")
        return redirect("estoque:transportadoras")
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao deletar a transportadora!")
        return redirect("estoque:transportadoras")
    messages.success(request, "Transportadora deletada com sucesso!")
    return redirect("estoque:transportadoras")
