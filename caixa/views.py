from django.shortcuts import render
from .models import Venda, ItemDoPedido
from django.views import View
from appkraft.models import Produtos
from django.db.models import Sum, F, FloatField, Q
from .forms import ItemDoPedidoForm
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
)


class CaixaView(View):

    def get(self, request):
        data = {}
        data['comandas'] = Venda.objects.filter(status=False).order_by("-pk")
        return render(request, 'caixa/home.html', data)

    def post(self, request):

        data = {}
        data['comandas'] = Venda.objects.filter(status=False).order_by("-pk")
        data['form_item'] = ItemDoPedidoForm()
        data['numero'] = request.POST['numero']
        data['desconto'] = float(request.POST['desconto'].replace(',','.'))
        # data['venda'] = request.POST['venda_id']
        data['venda'] = request.POST['venda_id']

        venda = ''
        if data['numero']:
            data['venda'] = data['numero']
            v = Venda.objects.get(id=int(data['venda']))
            if v.status == False:
                venda = v    


        else:
            venda = Venda.objects.create(
                numero = 0,
                desconto=data['desconto']
            )
            venda.numero = venda.id
            venda.save()

            # Venda.objects.filter(id=venda.id).update(numero=venda.id)

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
        return render(request, '/caixa/home.html')

    def post(self, request, venda):

        data = {}

        def checkqnt():
            if request.POST['quantidade'] == '' or None:
                qnt = 1
            else:
                qnt = request.POST['quantidade'] 
            return float(qnt)

        # print()

        item = ItemDoPedido.objects.filter(
            produto_id=request.POST['produto_id'],
            venda_id=venda
        ).first()
    
        if item:    

            qnt = item.quantidade + checkqnt()
            # ItemDoPedido.objects.filter(
            #     id=item.id
            # ).update(quantidade=qnt) 
            item = ItemDoPedido.objects.get(id=item.id) 
            item.quantidade = qnt
            item.save()

            # item = ItemDoPedido.objects.get(id=item.id)
            print('if', item.id)


        else:
            item = ItemDoPedido.objects.create(
                produto_id=request.POST['produto_id'],
                quantidade=checkqnt(),
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


        print('Item:', item.id, ' Venda valor:', data['venda_obj'].valor)


        if item:
            data['foto'] = Produtos.objects.get(
            id=item.produto_id
            )

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
            request, 'caixa/home.html', {'venda_id':venda_id}
            # request, 'caixa/home.html', data
        )
        # return HttpResponseRedirect(self.get_success_url())


# delete com ajax
def delete_post(request):
    if request.method == 'DELETE':
        print(QueryDict(request.body).get('postpk'))

        # post = Post.objects.get(
        #     pk=int(QueryDict(request.body).get('postpk')))

        item_pedido = ItemDoPedido.objects.get(id=int(QueryDict(request.body).get('postpk')))
        venda_id = item_pedido.venda.id
        item_pedido.delete()

        
        return render(
            request, 'caixa/home.html', {'venda_id':venda_id}
            # request, 'caixa/home.html', data
        )

        # post.delete()

    
    # else:
    #     return HttpResponse(
    #         json.dumps({"nothing to see": "this isn't happening"}),
    #         content_type="application/json"
    #     )

# finalizar com ajax
def finalizar_venda(request):
    if request.method == 'POST':
        print(QueryDict(request.body).get('postpk'))

        # post = Post.objects.get(
        #     pk=int(QueryDict(request.body).get('postpk')))

        venda = Venda.objects.get(id=int(QueryDict(request.body).get('postpk')))
        venda_id = venda.id
        venda.status = True
        venda.save()

        
        return render(
            request, 'caixa/home.html', {'venda_id':venda_id}
            # request, 'caixa/home.html', data
        )

        # post.delete()



class VendaListView(ListView):
    template_name='dashboard/venda_list.html'
    queryset=Venda.objects.all().order_by('-pk')

    def get_context_data(self, *args, **kwargs):
        context = super(VendaListView, self).get_context_data(*args, **kwargs)
        context['fechadas'] = self.queryset.filter(status=True)
        context['abertas'] = self.queryset.filter(status=False)
        return context

