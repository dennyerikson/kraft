from django.shortcuts import render, redirect
from .models import Produtos, Compra_Id, Compras
from django.db.models import Q
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from .forms import ProdutosModelForm
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)
from django.urls import reverse

lista = []
produto = []
# Create your views here.
@login_required
def home(request):
    global lista
    global produto
    """
    O Django segue o padrão MVC muito de perto, mas usa uma terminologia ligeiramente dierente. O django é 
    essencialmente um framework MTV(Model-Template-View). Usa o termo Templates para Views e Views para
    Controller. Em outras palavras, nas views do Django são chamados templates e controllers e são chamados 
    views. O código HTML estará em modelos e o código Python etará em Views e Models. 
    """
    
    if request.user.username == "kraft.products":
        url = 'produtos'
        return redirect('/{}'.format(url))
    
    else:
        # method GET
        search = request.GET.get('search')
        quantidade = request.GET.get('qnt')
        venda = request.GET.get('vnd')
            # get id produto
        if search:
            venda = int(venda)
            # try:
            vendas = Compra_Id.objects.get(pk=venda, status='Andamento')
            if vendas:
                produtos = Produtos.objects.filter(
                    Q(codigo_produto=search) |
                    Q(codigo_barras=search)
                )
                
                for p in produtos:
                    quantidade = int(quantidade)
                    if quantidade:
                        p.valor *= quantidade
                    else:
                        quantidade = 1

                    query = Compras.objects.create(
                        codigo_compra = vendas,
                        codigo_produto = p.codigo_produto,
                        nome = p.nome,
                        valor = p.valor,
                        quantidade = quantidade,
                    ).save()

            return redirect('/', {'venda':vendas.pk})

        # except:
        #     pass

        
       
        
        

    compras = Compras.objects.all()

        # lista = [{'codigo':item['codigo_produto'], 'nome':item['nome'], 'valor':item['valor']}
        #     for item in produtos
        # ]
        
        # lista = [
        #     produto.append(produto_serializer(item))
        #     for item in produtos
        # ]
        
        # for l in lista:
        #     produto.append(l)



    

        # retornar persitencia do produto

        # adicionar em lista

    # method POST
        # retornar Total
        
        # persistir compra


    context = {'lista':compras, 'venda':venda}
    return render(request, 'appkraft/home.html', context)


def produto_serializer(item):
    return {'codigo':item['codigo_produto'], 'nome':item['nome'], 'valor':item['valor']}


def produtos(request):

    produtos = Produtos.objects.all()

    if request.method=='POST':
        form = ProdutosModelForm(request.POST, request.FILES or None)

        if form.is_valid():
            query = form.save(commit=False)
            query.create_date = timezone.now()
            query.save()
            print('SUCESS')
            return redirect('/produtos/')
    else:
        form = ProdutosModelForm()

    context = {'produtos':produtos, 'form':form}
    return render(request, 'appkraft/produtos.html', context)

class ProdutosListView(ListView):
    template_name = 'appkraft/appkraft_list.html'
    queryset = Produtos.objects.all()


class ProdutosCreateView(CreateView):
    # template_name = 'appkraft/appkraft_create.html'
    template_name = 'appkraft/appkraft_create.html'
    form_class = ProdutosModelForm
    queryset = Produtos.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('appkraft:appkraft-list')


class ProdutosUpdateView(UpdateView):
    template_name = 'appkraft/appkraft_create.html'
    form_class = ProdutosModelForm
    queryset = Produtos.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Horario, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('appkraft:appkraft-list')



class ProdutosDeleteView(DeleteView):
    template_name = 'appkraft/appkraft_delete.html'
    form_class = ProdutosModelForm
    queryset = Produtos.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Horario, id=id_)
    
    def get_success_url(self):
        return reverse('appkraft:appkraft-list')