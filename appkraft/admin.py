from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Produtos)
admin.site.register(Compras)
admin.site.register(Compra_Id)

#models manager
# fonte https://github.com/marinho/aprendendo-django/blob/master/24-fazendo-mais-coisas-na-aplicacao-de-contas-pessoais.md
class ComprasManager(admin.ModelAdmin):
    list_diplay = ('codogo_compra','valor_total',)

