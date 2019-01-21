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
    foto = models.ImageField(upload_to='appkraft', null=True, blank=True)
    #campo validade


    def __str__(self):
        return self.nome