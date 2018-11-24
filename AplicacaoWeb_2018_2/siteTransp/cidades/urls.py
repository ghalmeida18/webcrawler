# Author Jose Diego Alves Duarte
from django.conf.urls import url
from siteTransp.cidades import views

urlpatterns = [

    url(r'^$', views.index, name='index'),  # url para a lista de cidades
    # url para a pagina da cidade que recebe uma ER com o parametro slug
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/relatorio', views.relatorio, name='relatorio'),
    url(r'^(?P<slug>[\w_-]+)/grafico', views.grafico, name='grafico'),
    url(r'^(?P<slug>[\w_-]+)/detalhado', views.detalhado, name='detalhado'),
    url(r'^(?P<slug>[\w_-]+)/anomalias', views.anomalias, name='anomalias'),

]
