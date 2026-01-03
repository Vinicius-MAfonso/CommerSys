from django.db import models


class Cliente(models.Model):
    TIPO_PESSOA_CHOICES = [("PF", "Pessoa Física"), ("PJ", "Pessoa Jurídica")]
    INDICADOR_IE_CHOICES = [
        (1, "Contribuinte ICMS"),
        (2, "Contribuinte Isento"),
        (3, "Não Contribuinte"),
    ]

    tipo_pessoa = models.CharField(
        max_length=2, choices=TIPO_PESSOA_CHOICES, default="PF"
    )
    cpf_cnpj = models.CharField(max_length=20, unique=True)
    
    nome_razao_social = models.CharField(max_length=150)
    nome_fantasia = models.CharField(max_length=150, blank=True, null=True)

    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)
    indicador_ie = models.IntegerField(choices=INDICADOR_IE_CHOICES, default=9)

    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    cep = models.CharField(max_length=15)
    uf = models.CharField(max_length=2)
    municipio = models.CharField(max_length=100)
    codigo_municipio = models.IntegerField()
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome_razao_social} ({self.cpf_cnpj})"


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
