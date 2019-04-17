from django.db import models

# Create your models here. importante prefetch_related
class Perfil(models.Model):

    perfil = models.CharField(max_length=30)

    def __str__(self):
        return self.perfil
        
    
class Pessoa(models.Model):
    perfil = models.ForeignKey(Perfil, blank=True, on_delete=models.PROTECT)
    # codigo = models.IntegerField()
    nome = models.CharField(max_length=150) 
    aniverssario = models.DateField(blank=True, null=True)

    # alterar para diminuir cadastro 
    contato = models.CharField(max_length=150) # contato completo tel, cel, email
    # celular = models.CharField(max_length=11)
    endereco = models.CharField(max_length=200) # endereço completo otimisar com api correios JS
    # numero = models.CharField(max_length=10)
    # bairro = models.CharField(max_length=50)
    # cidade = models.CharField(max_length=50)
    # cep = models.CharField(max_length=11)
    # uf = models.CharField(max_length=2)
    foto = models.ImageField(upload_to='accounts', blank=True, null=True)

    #perfil geral
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=50, blank=True, null=True)
    n_ie = models.CharField(max_length=50, blank=True, null=True)
    n_im = models.CharField(max_length=10, blank=True, null=True)

    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(
            self.nome,
            self.perfil
        )

    def get_absolute_url(self):
        return '/%s/' % self.id
        