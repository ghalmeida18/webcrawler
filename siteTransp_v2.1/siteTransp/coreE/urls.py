# Author Jose Diego Alves Duarte
from django.conf.urls import url
from siteTransp.coreE import views

urlpatterns = [

    url(r'^$', views.home, name='home'),  # url para a lista de cidades

]
