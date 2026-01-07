from django import forms
from django.forms import inlineformset_factory
from .models import Contato, Cliente, Pedido, ItemPedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            "cliente",
            "transportadora",
            "natureza_operacao",
            "meio_pagamento",
            "modalidade_frete",
            "peso_bruto",
            "peso_liquido",
            "quantidade_volumes",
        ]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control select2"}),
            "transportadora": forms.Select(attrs={"class": "form-control select2"}),
            "data_pedido": forms.DateTimeInput(attrs={"class": "form-control"}),
            "natureza_operacao": forms.TextInput(attrs={"class": "form-control"}),
            "meio_pagamento": forms.Select(attrs={"class": "form-control"}),
            "modalidade_frete": forms.Select(attrs={"class": "form-control"}),
            "peso_bruto": forms.TextInput(
                attrs={"class": "form-control decimal", "placeholder": "0,000"}
            ),
            "peso_liquido": forms.TextInput(
                attrs={"class": "form-control decimal", "placeholder": "0,000"}
            ),
            "quantidade_volumes": forms.NumberInput(attrs={"class": "form-control"}),
        }


class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = [
            "produto",
            "quantidade",
            "preco_unitario",
            "cfop",
            "icms_cst",
            "icms_aliquota",
            "icms_base_calculo",
        ]
        widgets = {
            "produto": forms.Select(attrs={"class": "form-control"}),
            "quantidade": forms.NumberInput(attrs={"class": "form-control"}),
            "preco_unitario": forms.TextInput(
                attrs={"class": "form-control moeda", "placeholder": "R$ 0,00"}
            ),
            "cfop": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "0000"}
            ),
            "icms_cst": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "000"}
            ),
            "icms_aliquota": forms.TextInput(
                attrs={"class": "form-control decimal", "placeholder": "0,00"}
            ),
            "icms_base_calculo": forms.TextInput(
                attrs={"class": "form-control moeda", "placeholder": "R$ 0,00"}
            ),
        }


ItemPedidoFormSet = inlineformset_factory(
    Pedido, ItemPedido, form=ItemPedidoForm, extra=1, can_delete=True
)


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
            "cpf_cnpj": forms.TextInput(
                attrs={
                    "class": "form-control cpf_cnpj",
                }
            ),
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
