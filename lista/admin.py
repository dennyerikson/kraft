from django.contrib import admin
from .models import Lista, ItemLista


class ItemDaListaInline(admin.TabularInline):
    model = ItemLista
    extra = 1

class ListaAdmin(admin.ModelAdmin):
    inlines = [ItemDaListaInline]


# Register your models here.
admin.site.register(Lista, ListaAdmin)


