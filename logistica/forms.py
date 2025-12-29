from django import forms
from .models import Produto, Transportadora
from django.core import validators


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco_base', 'ncm', 'unidade_medida', 'origem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preco_base': forms.TextInput(attrs={'class': 'form-control moeda', 'placeholder': 'R$ 0,00', 'maxlength': '11',}),
            'ncm': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '8'}),
            'unidade_medida': forms.Select(attrs={'class': 'form-control'}),
            'origem': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preco_base'].localize = True
        self.fields['preco_base'].widget.is_localized = True

class TransportadoraForm(forms.ModelForm):
    class Meta:
        model = Transportadora
        fields = ['razao_social', 'cnpj', 'inscricao_estadual', 'logradouro', 'municipio', 'uf']
        widgets = {
            'razao_social': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
        }