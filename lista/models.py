from django.db import models
from accounts.models import Pessoa
from appkraft.models import Produtos

# Create your models here.
class Lista(models.Model):
    lista = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.lista)
        

    def get_absolute_url(self):
        return '/%s/' % self.id

class ItemLista(models.Model):
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.FloatField()

    def __str__(self):
        return str(self.lista) +" - "+str(self.produto)

    def get_absolute_url(self):
        return '/%s/' % self.id


