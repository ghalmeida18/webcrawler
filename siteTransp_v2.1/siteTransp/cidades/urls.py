# Author Jose Diego Alves Duarte
from django.conf.urls import url
from siteTransp.cidades import views

urlpatterns = [

    url(r'^$', views.index, name='index'),  # url para a lista de cidades
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),# url para a pagina da cidade que recebe uma ER com o parametro slug

]
