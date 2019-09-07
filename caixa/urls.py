from django.urls import path, include
from . import views
from .views import (
    CaixaView,
    ItemDoPedidoView,
    ItemDoPedidoDelete,
    VendaListView,
)

# app_name = 'caixa'

urlpatterns = [
    path('', CaixaView.as_view(), name='caixa-view'),
    path('item-do-pedido/<int:venda>/', ItemDoPedidoView.as_view(), name='item-do-pedido'),
    path('item-delete-pedido/<int:item>/', ItemDoPedidoDelete.as_view(), name='item-delete-pedido'),
    path('delete_post/', views.delete_post, name="delete_post"),
    path('finalizar_venda/', views.finalizar_venda, name="finalizar_venda"),
    path('venda_list/', VendaListView.as_view(), name='venda-list'),
    path('setarmesa/', views.set_mesa, name='setar_mesa'),
]