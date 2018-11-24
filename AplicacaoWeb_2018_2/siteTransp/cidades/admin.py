# Author Jose Diego Alves Duarte
from django.contrib import admin

from .models import Cidade, Product, Empenho


class CidadeAdmin(admin.ModelAdmin):
    '''
        Admin View for Cidade
    '''
    list_display = ('nameCidade',)
    search_fields = ('nameCidade',)
    prepopulated_fields = {'slug': ('nameCidade',)}
    # list_filter = ('nameCidade',)  - apresenta uma lica de filtros


admin.site.register(Cidade, CidadeAdmin)


class EmpenhoAdmin(admin.ModelAdmin):
    '''
        Admin View for Cidade
    '''
    list_display = ('empID','empFuncao','empSubFuncao','empValor','empData')
    search_fields = ('empID', 'IdCliente', 'empFuncao',)
    # list_filter = ('nameCidade',)  - apresenta uma lica de filtros


admin.site.register(Empenho, EmpenhoAdmin)


# class ProjetoAdmin(admin.ModelAdmin):
#     '''
#         Admin View for Projeto
#     '''
#     list_display = ('nameProjeto', 'cidade', 'valor')
#     list_filter = ('cidade',)
#     prepopulated_fields = {'slug': ('nameProjeto',)}

# admin.site.register(Projeto, ProjetoAdmin)


class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    list_display = ('name', 'price')


admin.site.register(Product, ProductAdmin)
