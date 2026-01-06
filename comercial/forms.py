from django import forms
from .models import Contato, Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "cpf_cnpj",
            "nome_razao_social",
            "inscricao_estadual",
            "indicador_ie",
            "email",
            "telefone",
            "cep",
            "uf",
            "municipio",
            "codigo_municipio",
            "bairro",
            "logradouro",
            "numero",
            "complemento",
        ]
        widgets = {
            "cpf_cnpj": forms.TextInput(attrs={"class": "form-control cpf_cnpj",}),
            "inscricao_estadual": forms.TextInput(
                attrs={"class": "form-control ie", "placeholder": "000.000.000.000"}
            ),
            "nome_razao_social": forms.TextInput(attrs={"class": "form-control"}),

            "indicador_ie": forms.Select(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(
                attrs={"class": "form-control phone", "placeholder": "(00) 0000-0000"}
            ),
            "cep": forms.TextInput(
                attrs={"class": "form-control cep", "placeholder": "00000-000"}
            ),
            "uf": forms.TextInput(attrs={"class": "form-control"}),
            "municipio": forms.TextInput(attrs={"class": "form-control"}),
            "codigo_municipio": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "logradouro": forms.TextInput(attrs={"class": "form-control"}),
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "complemento": forms.TextInput(attrs={"class": "form-control"}),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = [
            "nome",
            "email",
            "telefone",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(
                attrs={"class": "form-control phone", "placeholder": "(00) 0000-0000"}
            ),
        }
