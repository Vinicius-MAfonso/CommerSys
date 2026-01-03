from django.db import models


class Produto(models.Model):
    ORIGEM_CHOICES = [
        (0, "Nacional"),
        (1, "Estrangeira - Importação direta"),
        (2, "Estrangeira - Adquirida no mercado interno"),
    ]
    MEDIDA_CHOICES = [(0, "UN"), (1, "KG"), (2, "PC"), (3, "L")]
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    preco_base = models.DecimalField(max_digits=10, decimal_places=2)

    ncm = models.CharField(max_length=10)
    unidade_medida = models.IntegerField(choices=MEDIDA_CHOICES, default=0)
    origem = models.IntegerField(choices=ORIGEM_CHOICES, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Transportadora(models.Model):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razao_social
