from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Cliente
import logging

logger = logging.getLogger(__name__)

def clientes(request):
    try:
        clientes = Cliente.objects.all()
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao carregar clientes!")
        clientes = []
    return render(request, "clientes/clientes.html", {"clientes": clientes})


def cliente_detail(request, pk):
    if request.method == "GET":
        try:
            cliente = Cliente.objects.get(pk=pk)
            data = {
                "id": cliente.id,
                "nome_razao_social":cliente.nome_razao_social, 
                "cpf_cnpj":cliente.cpf_cnpj, 
                "telefone_principal":cliente.telefone_principal, 
                "endereco":cliente.endereco, 
                "inscricao_estadual":cliente.inscricao_estadual,
            }
            return JsonResponse(data)
        except Cliente.DoesNotExist:
            return JsonResponse({"error": "Cliente não encontrado."}, status=404)
        except Exception as e:
            logger.exception(e)
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Método não permitido."}, status=405)

def cliente_create(request):
    try:
        nome_razao_social = request.POST.get("nome_razao_social")
        cpf_cnpj = request.POST.get("cpf_cnpj")
        telefone_principal = request.POST.get("telefone_principal")
        endereco = request.POST.get("endereco")
        inscricao_estadual = request.POST.get("inscricao_estadual")
        Cliente.objects.create(nome_razao_social=nome_razao_social, cpf_cnpj=cpf_cnpj, telefone_principal=telefone_principal, endereco=endereco, inscricao_estadual=inscricao_estadual)
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao criar o cliente!")
        return redirect("comercial:clientes")
    messages.success(request, "Cliente criado com sucesso!")
    return redirect("comercial:clientes")


def cliente_update(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        cliente.nome_razao_social = request.POST.get("nome_razao_social")
        cliente.cpf_cnpj = request.POST.get("cpf_cnpj")
        cliente.telefone_principal = request.POST.get("telefone_principal")
        cliente.endereco = request.POST.get("endereco")
        cliente.inscricao_estadual = request.POST.get("inscricao_estadual")
        cliente.save()
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
        return redirect("comercial:clientes")
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao atualizar o cliente!")
        return redirect("comercial:clientes")
    messages.success(request, "Cliente atualizado com sucesso!")
    return redirect("comercial:clientes")


def cliente_delete(request, pk):
    try:
        cliente = Cliente.objects.get(pk=pk)
        cliente.delete()
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
        return redirect("comercial:clientes")
    except Exception as e:
        logger.exception(e)
        messages.error(request, f"Erro ao deletar o cliente!")
        return redirect("comercial:clientes")
    messages.success(request, "Cliente deletado com sucesso!")
    return redirect("comercial:clientes")


def contatos(request):
    pass
def contato_detail(request, pk):
    pass
def contato_criar(request):
    pass
def contato_update(request, pk):
    pass
def contato_delete(request, pk):
    pass

def pedidos(request):
    pass
def pedido_detail(request, pk):
    pass
def pedido_criar(request):
    pass
def pedido_update(request, pk):
    pass
def pedido_delete(request, pk):
    pass
