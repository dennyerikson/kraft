from django.db import models
from accounts.models import Pessoa
from appkraft.models import Produtos
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum, F, FloatField

class Mesa(models.Model):
    mesa = models.IntegerField()
    status = models.BooleanField(default=False)
    observacao = models.TextField(max_length=190)

    def __str__(self):
        return str(self.mesa)


class Table(models.Model):
    mesa = models.IntegerField()
    status = models.BooleanField(default=False)
    observacao = models.TextField(max_length=190)

    def __str__(self):
        return str(self.mesa)


# Create your models here.
class Venda(models.Model):
    numero = models.IntegerField()
    valor = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    funcionario = models.ForeignKey(Pessoa, blank=True, null=True, on_delete=models.PROTECT)
    status = models.BooleanField(default=False)
    create_date = models.DateField(
        auto_now=True
    )
    mesa = models.ForeignKey(Table, blank=True, null=True, on_delete=models.CASCADE)


    def calcular_total(self):
        total = self.itemdopedido_set.all().aggregate(
            total_pedido=Sum(
                (F('quantidade') * F('produto__valor')) - F('desconto'),
                output_field=FloatField()
            )
        )['total_pedido'] or 0

        total = float(total - ((total * float(self.desconto)/100)))
        self.valor = total
        print('model', self.valor)
        try:
            Venda.objects.filter(id=self.id).update(valor=self.valor)
            print('salvou')
        except:
            print('pass')

        
    def update_estoque(self):

        data = []
        for produto in self.itemdopedido_set.all():
            estoque = Produtos.objects.values('estoque_atual').get(id=produto.produto_id)['estoque_atual']
            data.append((produto.produto_id, produto.quantidade, estoque))              
        print(data)

        print(self.status)
        # pecorre lista desconta e atualiza estoque
        if self.status:
            for [id, quantidade, estoque] in data:
                estoque_atual = estoque - quantidade
                Produtos.objects.filter(id=id).update(estoque_atual=estoque_atual)
                print(Produtos.objects.filter(id=id))


    def __str__(self):
        return str(self.numero)



class ItemDoPedido(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.FloatField()
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return str(self.venda.numero) + " - " + self.produto.nome



@receiver(post_save, sender=ItemDoPedido)
def update_venda_total(sender, instance, **kwargs):
    instance.venda.calcular_total()

@receiver(pre_save, sender=ItemDoPedido)
def update_venda_total_pre(sender, instance, **kwargs):
    instance.venda.calcular_total()

@receiver(post_delete, sender=ItemDoPedido)
def update_venda_total_pre(sender, instance, **kwargs):
    instance.venda.calcular_total()

@receiver(post_save, sender=ItemDoPedido)
def update_estoque_total(sender, instance, **kwargs):
    instance.venda.update_estoque()


@receiver(post_save, sender=Venda)
def update_venda_total2(sender, instance, **kwargs):
    instance.calcular_total()

@receiver(post_save, sender=Venda)
def update_estoque_total2(sender, instance, **kwargs):
    instance.update_estoque()


