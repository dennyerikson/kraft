from django.db import models
from django.utils import timezone
from accounts.models import Pessoa



# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    estoque_atual = models.IntegerField()
    estoque_minimo = models.IntegerField()
    observacoes = models.TextField(max_length=255, null=True, blank=True)
    create_data = models.DateTimeField(
        default=timezone.now, blank=True, null=True
    )
    #campo imagem
    foto = models.ImageField(upload_to='appkraft', blank=True, null=True)
    #campo validade
    #dados de compra do produto
    empresa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    custo = models.DecimalField(max_digits=5, decimal_places=2)
    ganho = models.DecimalField(max_digits=5, decimal_places=2) #ganho em porcentagem

    def stoque_min(self):
        if self.estoque_minimo < 30:
            return "Estoque baixo de mais"


    def __str__(self):
        return self.nome



class Compra_Id(models.Model):
    STATUS = [
        ('Andamento','Andamento'),
        ('Finalizada','Finalizada'),
        ('Orçamento','Orçamento')
    ]

    status = models.CharField(max_length=10, choices=STATUS)
    create_date = models.DateTimeField(
        default=timezone.now
    )
    def __str__(self):
        return str(self.pk)



class ComprasManager(models.Manager):
    def get_query_set(self):
        query_set = super(ComprasManager, self).get_query_set()

        return query_set.extra(
            select = {
                '_valor_total':"""select sum(valor) from appkraft_compras
                where appkraft_compras.codigo_compra=1""",
            }
        )

class Compras(models.Model):
    codigo_compra = models.ForeignKey(Compra_Id, on_delete=models.CASCADE)
    codigo_produto = models.IntegerField()    
    nome = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)    
    create_data = models.DateTimeField(
        default=timezone.now, blank=True, null=True
    )
    # quantidade = models.IntegerField()
    # def calcular_total(self):
    #     total = 0
    #     for valor in self.all():
    #         total += self.valor
    #     return total


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return '/%s/' % self.id

    def valor_total(self):
        return self._valor_total

