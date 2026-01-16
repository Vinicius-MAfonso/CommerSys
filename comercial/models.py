from django.db import models
from logistica.models import Produto, Transportadora


class Cliente(models.Model):
    INDICADOR_IE_CHOICES = [
        (1, "Contribuinte ICMS"),
        (2, "Contribuinte Isento"),
        (3, "Não Contribuinte"),
    ]

    cpf_cnpj = models.CharField(max_length=20, unique=True, blank=True, null=True)

    nome_razao_social = models.CharField(max_length=150)

    inscricao_estadual = models.CharField(max_length=50, blank=True, null=True)
    indicador_ie = models.IntegerField(choices=INDICADOR_IE_CHOICES, default=9)

    email = models.EmailField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    cep = models.CharField(max_length=15, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    codigo_municipio = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    logradouro = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_razao_social


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    TIPO_FRETE_CHOICES = [
        (0, "Por conta do emitente"),
        (1, "Por conta do destinatário"),
        (2, "Por conta de terceiros"),
        (9, "Sem frete"),
    ]

    MEIO_PAGAMENTO_CHOICES = [
        ("01", "Dinheiro"),
        ("02", "Cheque"),
        ("03", "Cartão de Crédito"),
        ("04", "Cartão de Débito"),
        ("15", "Boleto Bancário"),
        ("17", "PIX"),
    ]

    STATUS_NFE_CHOICES = [
        ("pendente", "Pendente de Envio"),
        ("autorizada", "Autorizada"),
        ("rejeitada", "Rejeitada"),
        ("cancelada", "Cancelada"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    contato = models.ForeignKey(
        Contato, on_delete=models.SET_NULL, null=True, blank=True
    )
    transportadora = models.ForeignKey(
        Transportadora, on_delete=models.SET_NULL, null=True, blank=True
    )
    data_pedido = models.DateTimeField()

    natureza_operacao = models.CharField(max_length=100, default="Venda de Mercadoria")
    meio_pagamento = models.CharField(
        max_length=2, choices=MEIO_PAGAMENTO_CHOICES, default="01"
    )

    modalidade_frete = models.IntegerField(choices=TIPO_FRETE_CHOICES, default=9)
    peso_bruto = models.DecimalField(max_digits=10, decimal_places=3)
    peso_liquido = models.DecimalField(max_digits=10, decimal_places=3)
    quantidade_volumes = models.IntegerField(default=1)

    nfe_status = models.CharField(
        max_length=20, choices=STATUS_NFE_CHOICES, default="pendente"
    )
    nfe_chave = models.CharField(max_length=44, blank=True, null=True)
    nfe_numero = models.IntegerField(blank=True, null=True)
    nfe_serie = models.IntegerField(blank=True, null=True)
    nfe_protocolo = models.CharField(max_length=50, blank=True, null=True)
    nfe_motivo_rejeicao = models.TextField(blank=True, null=True)

    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome_razao_social}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name="itens", on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    cfop = models.CharField(max_length=4)
    icms_cst = models.CharField(
        max_length=3, default="101"
    )
    icms_aliquota = models.DecimalField(max_digits=5, decimal_places=2)
    icms_base_calculo = models.DecimalField(
        max_digits=10, decimal_places=2
    )

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
