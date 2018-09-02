# Author Jose Diego Alves Duarte
from django.shortcuts import render
from .models import Cidade

# imports para views para charts
import json
from .models import Product

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# importando o formulario de pesquisa
from .forms import SearchForm

# imports para python-mysql
import pymysql.cursors
import simplejson


def index(request):

    cidades_list = Cidade.objects.all()
    template_name = 'tcidades/index2.html'
    paginator = Paginator(cidades_list, 2)

    page = request.GET.get('page')
    try:
        cidades = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        cidades = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        cidades = paginator.page(paginator.num_pages)

    contexto = {
        'cidades': cidades
    }
    return render(request, template_name, contexto)


def details(request, slug):

    queryset = Product.objects.all()
    names = [obj.name for obj in queryset]
    prices = [int(obj.price) for obj in queryset]
    cidades = Cidade.objects.get(slug=slug)
    contexto = {}
    is_valid = False
    # data_Final = None
    # data_Inicial = None
    s = None

    # logica para o forms
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            is_valid = True
            # data_Final = form.cleaned_data['dataFinal']
            # data_Inicial = form.cleaned_data['dataInicial']
            s = form.soma()
            form = SearchForm(None)
    else:
        form = SearchForm()


    contexto = {
        'cidade': cidades,
        'names': json.dumps(names),
        'prices': json.dumps(prices),
        'form': form,
        'is_valid': is_valid,
        'soma': s,
    }


    template_name = 'tcidades/details2.html'
    return render(request, template_name, contexto)
