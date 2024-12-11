from django.contrib import admin
from .models import Produto


# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_filter = ['produto_parte', 'cor_nome', 'cor_hex', 'ativo']