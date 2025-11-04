from django.db import models

class Cliente(models.Model):
    nome_razao_social = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefone_principal = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome_razao_social

class Contato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contatos')
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cliente.nome_razao_social})"