from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome

class ValorDiferente(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey('comercial.Cliente', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - {self.cliente} - R${self.preco}"
    
class Transportadora(models.Model):
    nome = models.CharField(max_length=150)