from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
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
