from django import forms
from .models import Produto, Transportadora


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "descricao", "preco_base", "ncm", "unidade_medida", "origem"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "preco_base": forms.TextInput(
                attrs={
                    "class": "form-control moeda",
                    "placeholder": "R$ 0,00",
                    "maxlength": "11",
                }
            ),
            "ncm": forms.TextInput(
                attrs={"class": "form-control ncm", "placeholder": "0000.00.00"}
            ),
            "unidade_medida": forms.Select(attrs={"class": "form-control"}),
            "origem": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["preco_base"].localize = True
        self.fields["preco_base"].widget.is_localized = True


class TransportadoraForm(forms.ModelForm):
    class Meta:
        model = Transportadora
        fields = [
            "nome",
            "email",
            "telefone",
            "cnpj",
            "inscricao_estadual",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "telefone": forms.TextInput(
                attrs={"class": "form-control phone", "placeholder": "(00) 0000-0000"}
            ),
            "cnpj": forms.TextInput(
                attrs={
                    "class": "form-control cnpj",
                    "placeholder": "00.000.000/0000-00",
                }
            ),
            "inscricao_estadual": forms.TextInput(
                attrs={"class": "form-control ie", "placeholder": "000.000.000.000"}
            ),
        }
