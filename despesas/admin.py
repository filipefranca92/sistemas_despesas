from django.contrib import admin
from .models import Despesa, Categoria, FormaDePagamento, Renda

# Registra os modelos para que apareçam no Painel de Administração
admin.site.register(Categoria)
admin.site.register(FormaDePagamento)
admin.site.register(Despesa)
admin.site.register(Renda)