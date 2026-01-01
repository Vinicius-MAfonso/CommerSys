from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome