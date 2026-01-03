from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Contato, Cliente
from .forms import ContatoForm, ClienteForm

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
