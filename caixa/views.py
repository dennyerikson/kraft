from django.shortcuts import render
from .models import Venda, ItemDoPedido
from django.views import View
from appkraft.models import Produtos
from django.db.models import Sum, F, FloatField
from .forms import ItemDoPedidoForm


class CaixaView(View):

    def get(self, request):
        return render(request, 'caixa/home.html')

    def post(self, request):

        data = {}
        data['form_item'] = ItemDoPedidoForm()
        data['numero'] = request.POST['numero']
        data['desconto'] = float(request.POST['desconto'].replace(',','.'))
        # data['venda'] = request.POST['venda_id']
        data['venda'] = request.POST['venda_id']

        if data['venda']:
            venda = Venda.objects.get(id=int(data['venda']))            
        else:
            venda = Venda.objects.create(
                numero = 0,
                desconto=data['desconto']
            )

            Venda.objects.filter(id=venda.id).update(numero=venda.id)

        itens = venda.itemdopedido_set.all().annotate(
            total_item=Sum(
                (F('quantidade') * F('produto__valor')) - F('desconto'),
                output_field=FloatField()
            )
        ).order_by('-pk')
        

        data['venda_obj'] = venda
        data['itens'] = itens

        if itens:
            data['foto'] = Produtos.objects.get(
            id=itens.values('produto__id').first()['produto__id']
            )

        return render(request, 'caixa/home.html', data)


class ItemDoPedidoView(View):
    def get(self, request, pk):
        pass

    def post(self, request, venda):

        data = {}

        item = ItemDoPedido.objects.create(
            produto_id=request.POST['produto_id'],
            quantidade=request.POST['quantidade'],
            # desconto=float(request.POST['desconto'].replace(',','.')),
            venda_id=venda
        )

        data['item'] = item
        data['form_item'] = ItemDoPedidoForm()
        data['numero'] = item.venda.numero
        data['desconto'] = item.venda.desconto
        data['venda_obj'] = item.venda
        # data['venda_obj'] = venda
        data['itens'] = item.venda.itemdopedido_set.all().annotate(
            total_item=Sum(
                (F('quantidade') * F('produto__valor')) - F('desconto'),
                output_field=FloatField()
            )
        ).order_by('-pk')

        print('venda.item', data['venda_obj'].valor)

        if item:
            data['foto'] = Produtos.objects.get(
            id=item.produto_id
            )
            print(data['foto'].foto.url)

        return render(
            request, 'caixa/home.html', data
        )

class ItemDoPedidoDelete(View):
    def get(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        return render(
            request, 'caixa/home.html', {'item_pedido':item_pedido}
        )

    
    def post(self, request, item):
        item_pedido = ItemDoPedido.objects.get(id=item)
        venda_id = item_pedido.venda.id
        item_pedido.delete()

        return render(
            request, 'caixa/home.html', {'item_pedido':item_pedido}
        )