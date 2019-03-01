from django.urls import path
from . import views
from .views import CaixaView, ItemDoPedidoView, ItemDoPedidoDelete


urlpatterns = [
    path('', CaixaView.as_view(), name='caixa-view'),
    path('item-do-pedido/<int:venda>/', ItemDoPedidoView.as_view(), name='item-do-pedido'),
    path('item-delete-pedido/<int:item>/', ItemDoPedidoDelete.as_view(), name='item-delete-pedido'),
]