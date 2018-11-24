# Author Jose Diego Alves Duarte
from django.db import models
# import para charts
# from __future__ import unicode_literals

# filtro personalizado para o Manager


class CidadeManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(nameCidade__icontains=query) |
            models.Q(description__icontains=query)
        )


# class Projeto(models.Model):

#     nameProjeto = models.TextField('Projeto',unique=True, max_length=100)
#     slug = models.SlugField('Identificador')
#     description = models.TextField('Descrição', blank=True)
#     valor = models.DecimalField(max_digits=5, decimal_places=2)
#     cidade = models.ForeignKey('cidades.Cidade', verbose_name='Cidade')

#     class Meta:
#         verbose_name = "Projeto"
#         verbose_name_plural = "Projetos"
#         ordering = ['nameProjeto']

#     def __str__(self):
#         return self.nameProjeto

# ==========================================================
# class para representar as cidades envolvidas
class Cidade(models.Model):
    idCliente = models.IntegerField('idCliente')
    nameCidade = models.CharField('Cidade', max_length=100, unique=True)
    slug = models.SlugField('Identificador')
    description = models.TextField('Descrição', blank=True, null=True)
    about = models.TextField('Sobre a cidade', blank=True, null=True)
    image = models.ImageField(upload_to='cidades/images',
                              verbose_name='Imagem', null=True, blank=True
                              )

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['nameCidade']

    def __str__(self):
        return self.nameCidade

    def get_absolute_url(self):
        return reverse('cidades:cidade', kwargs={'slug': self.slug})
# fim da class
# ==========================================================


# ==========================================================
# class para representar os dados de empenho
class Empenho(models.Model):
    empID = models.IntegerField('ID', null=True)
    empOrgao = models.CharField('Orgao', max_length=100)
    empData = models.CharField('Data', max_length=100)
    empValor = models.DecimalField(
        'Valor', max_digits=15, decimal_places=2)
    empIdFav = models.CharField('IdFav', max_length=100)
    empFuncao = models.CharField('Funcao', max_length=200)
    empSubFuncao = models.CharField('SubFuncao', max_length=200, null=True)
    idCliente = models.IntegerField('Cliente')

    def __str__(self):
        return str(self.empID) + self.empOrgao + self.empFuncao + str(self.empValor)
# fim da class
# ==========================================================


# ==========================================================
# models teste para charts
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
# ==========================================================
