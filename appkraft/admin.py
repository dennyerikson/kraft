from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Produtos)
admin.site.register(Compras)
admin.site.register(Compra_Id)

class ComprasManager(admin.ModelAdmin):
    list_diplay = ('codogo_compra','valor_total',)

