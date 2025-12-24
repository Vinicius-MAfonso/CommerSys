from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto
from .forms import ProdutoForm

class ProdutoListView(ListView):
    model = Produto
    template_name = 'logistica/produto_list.html'
    context_object_name = 'produtos'

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'logistica/produto_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'logistica/produto_form.html'
    success_url = reverse_lazy('logistica:produtos')

class ProdutoUpdateView(UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'logistica/produto_form.html'
    
    def get_success_url(self):
        return reverse_lazy('logistica:produto_detail', kwargs={'pk': self.object.pk})

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'logistica/produto_confirm_delete.html'
    success_url = reverse_lazy('logistica:produtos')