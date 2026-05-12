from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Produto, Transportadora
from .forms import ProdutoForm, TransportadoraForm


class ProdutoListView(ListView):
    model = Produto
    template_name = "logistica/produto_list.html"
    context_object_name = "produtos"


class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "logistica/produto_form.html"
    success_url = reverse_lazy("logistica:produtos")


class ProdutoDetailView(DetailView):
    model = Produto
    template_name = "logistica/produto_detail.html"
    context_object_name = "produto"


class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "logistica/produto_form.html"

    def get_success_url(self):
        return reverse_lazy("logistica:produto_detail", kwargs={"pk": self.object.pk})


class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy("logistica:produtos")


class TransportadoraListView(ListView):
    model = Transportadora
    template_name = "logistica/transportadora_list.html"
    context_object_name = "transportadoras"


class TransportadoraCreateView(CreateView):
    model = Transportadora
    form_class = TransportadoraForm
    template_name = "logistica/transportadora_form.html"
    success_url = reverse_lazy("logistica:transportadoras")


class TransportadoraDetailView(DetailView):
    model = Transportadora
    template_name = "logistica/transportadora_detail.html"
    context_object_name = "transportadora"


class TransportadoraUpdateView(UpdateView):
    model = Transportadora
    form_class = TransportadoraForm
    template_name = "logistica/transportadora_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "logistica:transportadora_detail", kwargs={"pk": self.object.pk}
        )


class TransportadoraDeleteView(DeleteView):
    model = Transportadora
    success_url = reverse_lazy("logistica:transportadoras")


@require_http_methods(["GET"])
def api_produtos_list(request):
    """
    API endpoint to fetch all active products with relevant details for order items.
    Returns JSON with product list.
    """
    try:
        produtos = Produto.objects.all().values(
            'id',
            'nome',
            'descricao',
            'preco_base',
            'peso_unitario',
            'ncm',
            'cest',
            'cfop_padrao',
            'unidade_medida',
            'origem'
        )
        
        produtos_list = list(produtos)
        
        return JsonResponse({
            'success': True,
            'produtos': produtos_list,
            'total': len(produtos_list)
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)


@require_http_methods(["GET"])
def api_produto_detail(request, produto_id):
    """
    API endpoint to fetch a single product's details.
    Returns JSON with product information.
    """
    try:
        produto = Produto.objects.get(id=produto_id)
        
        return JsonResponse({
            'success': True,
            'produto': {
                'id': produto.id,
                'nome': produto.nome,
                'descricao': produto.descricao,
                'preco_base': float(produto.preco_base),
                'ncm': produto.ncm,
                'cest': produto.cest,
                'cfop_padrao': produto.cfop_padrao,
                'unidade_medida': produto.get_unidade_medida_display(),
                'origem': produto.get_origem_display(),
            }
        })
    except Produto.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Produto não encontrado'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

