from django.db import models
from django.utils import timezone

# Create your models here.
class Produtos(models.Model):
    codigo_produto = models.IntegerField(unique=True)
    codigo_barras = models.IntegerField(unique=True)
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    marca = models.CharField(max_length=150)
    estoque_atual = models.IntegerField()
    estoque_minimo = models.IntegerField()
    observacoes = models.TextField(null=True, blank=True)
    create_data = models.DateTimeField(
        default=timezone.now, blank=True, null=True
    )
    #campo imagem
    foto = models.ImageField(upload_to='appkraft', blank=True, null=True)
    #campo validade


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

class Compras(models.Model):
    codigo_compra = models.ForeignKey(Compra_Id, on_delete=models.CASCADE)
    codigo_produto = models.IntegerField()    
    nome = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)    
    create_data = models.DateTimeField(
        default=timezone.now, blank=True, null=True
    )
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return '/%s/' % self.id

