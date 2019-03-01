from django import forms
from .models import ItemDoPedido
from django.forms import widgets


class ItemDoPedidoForm(forms.Form):
    produto_id = forms.CharField(label='ID Produto', max_length=100)
    quantidade = forms.DecimalField(label='QNT Produto', max_digits=7, decimal_places=2)
    # desconto = forms.DecimalField(label='Desconto', max_digits=7, decimal_places=2)


