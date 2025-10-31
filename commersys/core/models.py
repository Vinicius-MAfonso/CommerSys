from django.db import models

class Cliente(models.Model):
    nome_razao = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=20, unique=True, blank=True, null=True)
    telefone_principal = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome_razao

class Contato(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contatos')
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cliente.nome_razao})"

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente =  models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    contato = models.ForeignKey(Contato, on_delete=models.SET_NULL, blank=True, null=True)
    data_pedido = models.DateField()
    valor_total = models.DecimalField(decimal_places=2, default=0)
    forma_pagamento = models.CharField(max_length=20, blank=True, null=True)
    nf = models.CharField(max=10, blank=True, null=True)
    forma_entrega = models.CharField(max_length=20, blank=True, null=True)
    arquivo_adicional = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.cliente.nome_razao})"

class ItemPedido(models.Model):
    pedido = models.models.ForeignKey(Pedido, on_delete=models.CASCADE)   