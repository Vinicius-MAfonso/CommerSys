from django.contrib import admin
from .models import Produto, Transportadora, TabelaPrecoCliente

admin.site.register(Produto)
admin.site.register(Transportadora)
admin.site.register(TabelaPrecoCliente)
admin.site.site_header = "Administração do Estoque"