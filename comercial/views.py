from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Contato
from .forms import ContatoForm


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
