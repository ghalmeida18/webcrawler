# Author Jose Diego Alves Duarte
from django.contrib import admin

from .models import Cidade, Orgao, Projeto, Product


class CidadeAdmin(admin.ModelAdmin):
    '''
        Admin View for Cidade
    '''
    list_display = ('nameCidade',)
    search_fields = ('nameCidade',)
    prepopulated_fields = {'slug': ('nameCidade',)}
    # list_filter = ('nameCidade',)  - apresenta uma lica de filtros


admin.site.register(Cidade, CidadeAdmin)


class OrgaoAdmin(admin.ModelAdmin):
    '''
        Admin View for Orgao
        '''
    list_display = ('nameOrgao',)
    prepopulated_fields = {'slug': ('nameOrgao',)}


admin.site.register(Orgao, OrgaoAdmin)


class ProjetoAdmin(admin.ModelAdmin):
    '''
        Admin View for Projeto
    '''
    list_display = ('nameProjeto', 'cidade', 'orgao', 'valor')
    list_filter = ('cidade',)
    prepopulated_fields = {'slug': ('nameProjeto',)}


admin.site.register(Projeto, ProjetoAdmin)


class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    list_display = ('name', 'price')


admin.site.register(Product, ProductAdmin)
