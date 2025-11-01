from django.contrib import admin
from .models import Cliente, Contato, Produto, Pedido, ItemPedido, PrecoPersonalizado

# -------------------------
# Inline de Contatos dentro do Cliente
# -------------------------
class ContatoInline(admin.TabularInline):
    model = Contato
    extra = 1  # Mostra 1 linha vazia para adicionar novo contato
    fields = ('nome', 'telefone', 'email')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_razao', 'cpf_cnpj', 'telefone_principal')
    search_fields = ('nome_razao', 'cpf_cnpj')
    inlines = [ContatoInline]


# -------------------------
# Inline de Itens dentro do Pedido
# -------------------------
class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1
    fields = ('produto', 'quantidade', 'subtotal')
    readonly_fields = ('subtotal',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_pedido', 'valor_total', 'forma_pagamento')
    list_filter = ('data_pedido', 'forma_pagamento')
    search_fields = ('cliente__nome_razao',)
    date_hierarchy = 'data_pedido'
    inlines = [ItemPedidoInline]


# -------------------------
# Admin de Produto
# -------------------------
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)


# -------------------------
# Admin de Preço Personalizado
# -------------------------
@admin.register(PrecoPersonalizado)
class PrecoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'preco_especial')
    search_fields = ('cliente__nome_razao', 'produto__nome')
