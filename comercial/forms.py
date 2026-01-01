from django import forms
from .models import Contato


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
