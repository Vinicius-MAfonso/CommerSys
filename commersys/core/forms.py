from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome_razao", "cpf_cnpj", "telefone_principal", "endereco"]
        