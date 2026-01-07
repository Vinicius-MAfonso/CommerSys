from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.db import transaction
from .models import Contato, Cliente, Pedido
from .forms import ContatoForm, ClienteForm, PedidoForm, ItemPedidoFormSet

class PedidoListView(ListView):
    model = Pedido
    template_name = "comercial/pedido_list.html"
    context_object_name = "pedidos"

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = "comercial/pedido_detail.html"
    context_object_name = "pedido"

class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = "comercial/pedido_form.html"
    success_url = reverse_lazy("comercial:pedidos")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['itens'] = ItemPedidoFormSet(self.request.POST)
        else:
            data['itens'] = ItemPedidoFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        itens = context['itens']
        with transaction.atomic():
            self.object = form.save()
            if itens.is_valid():
                itens.instance = self.object
                itens.save()
            else:
                return self.form_invalid(form)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ClienteListView(ListView):
    model = Cliente
    template_name = "comercial/cliente_list.html"
    context_object_name = "clientes"


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "comercial/cliente_form.html"
    success_url = reverse_lazy("comercial:clientes")


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "comercial/cliente_detail.html"
    context_object_name = "cliente"


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "comercial/cliente_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "comercial:cliente_detail", kwargs={"pk": self.object.pk}
        )


class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("comercial:clientes")

class ContatoListView(ListView):
    model = Contato
    template_name = "comercial/contato_list.html"
    context_object_name = "contatos"


class ContatoCreateView(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = "comercial/contato_form.html"
    success_url = reverse_lazy("comercial:contatos")


class ContatoDetailView(DetailView):
    model = Contato
    template_name = "comercial/contato_detail.html"
    context_object_name = "contato"


class ContatoUpdateView(UpdateView):
    model = Contato
    form_class = ContatoForm
    template_name = "comercial/contato_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "comercial:contato_detail", kwargs={"pk": self.object.pk}
        )


class ContatoDeleteView(DeleteView):
    model = Contato
    success_url = reverse_lazy("comercial:contatos")
