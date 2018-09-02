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


class Projeto(models.Model):

    nameProjeto = models.TextField('Projeto', max_length=100)
    orgao = models.ForeignKey('cidades.Orgao', verbose_name='Orgão')
    slug = models.SlugField('Identificador')
    description = models.TextField('Descrição', blank=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    cidade = models.ForeignKey('cidades.Cidade', verbose_name='Cidade')

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
        ordering = ['nameProjeto']

    def __str__(self):
        return self.nameProjeto


class Orgao(models.Model):

    nameOrgao = models.TextField('Orgao', max_length=100, unique=True)
    slug = models.SlugField('Identificador')
    description = models.TextField('Descrição', blank=True)
    # metodo com foreignkey tem que vir antes, pq ??? no sei kk
    cidade = models.ForeignKey('cidades.Cidade', verbose_name='Cidade')

    class Meta:
        verbose_name = "Orgao"
        verbose_name_plural = "Orgaos"
        ordering = ['nameOrgao']

    def __str__(self):
        return self.nameOrgao


class Cidade(models.Model):

    nameCidade = models.CharField('Cidade', max_length=100)
    slug = models.SlugField('Identificador')
    description = models.TextField('Descrição', blank=True)
    about = models.TextField('Sobre a cidade', blank=True)
    image = models.ImageField(upload_to='cidades/images',
                              verbose_name='Imagem', null=True, blank=True
                              )

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['nameCidade']

    def __str__(self):
        return self.nameCidade


# ==========================================================
# models teste para charts
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name
