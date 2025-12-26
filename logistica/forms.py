from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco_base', 'ncm', 'unidade_medida', 'origem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'preco_base': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0,00'}),
            'ncm': forms.TextInput(attrs={'class': 'form-control'}),
            'unidade_medida': forms.Select(attrs={'class': 'form-control'}),
            'origem': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preco_base'].localize = True
        self.fields['preco_base'].widget.is_localized = True