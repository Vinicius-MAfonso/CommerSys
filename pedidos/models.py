from django.db import models
from clientes.models import Cliente, Contato
from produtos.models import Produto

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    contato = models.ForeignKey(Contato, on_delete=models.SET_NULL, blank=True, null=True)
    data_pedido = models.DateTimeField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    forma_pagamento = models.CharField(max_length=50, blank=True, null=True)
    nota_fiscal = models.CharField(max_length=20, blank=True, null=True)
    forma_entrega = models.CharField(max_length=100, blank=True, null=True)
    arquivo_adicional = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome_razao_social}"
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Pedido # {self.produto.id})"