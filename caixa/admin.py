from django.contrib import admin
from .models import Venda, ItemDoPedido

class ItemDoPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ['valor']
    inlines = [ItemDoPedidoInline]
    list_display=['id','numero', 'funcionario', 'status']

# Register your models here.
admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)