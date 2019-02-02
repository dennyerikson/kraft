from django.db import models

# Create your models here. importante prefetch_related
class Perfil(models.Model):

    perfil = models.CharField(max_length=30)

    def __str__(self):
        return self.perfil
        
    
class Pessoa(models.Model):
    perfil = models.ManyToManyField(Perfil)
    codigo = models.IntegerField()
    nome = models.CharField(max_length=150)
    aniversario = models.DateField()

    telefone = models.CharField(max_length=10)
    celular = models.CharField(max_length=11)
    endereco = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=11)
    uf = models.CharField(max_length=2)

    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=50)
    n_ie = models.CharField(max_length=50)
    n_im = models.CharField(max_length=10)

    descricao = models.TextField()

    def __str__(self):
        print(self.perfil)
        return '{} - {}'.format(
            self.nome,
            self.perfil
        )
        