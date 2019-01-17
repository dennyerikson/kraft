from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=150)