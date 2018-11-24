# Author Jose Diego Alves Duarte
import statistics

from operator import itemgetter
from django.shortcuts import render, get_object_or_404, Http404
from .models import Cidade
from .classes import SearchClasses, converterData
from datetime import datetime as dt

# imports para views para charts
import json
from django.utils.formats import localize
import locale
# importando o formulario de pesquisa
from .forms import SearchForm, listaDasCidades
from .forms import populTotal

# imports para python-mysql
import pymysql.cursors
x = "2001/12/12"
from django.views import generic
data_Final = None
data_Inicial = None
# CODIGO PARA ACESSO MYSQL
con = pymysql.connect(host='127.0.0.1',
                      user='root',  # insira aqui o seu usuario, é root?
                      passwd='jose123',  # insira aqui a senha so seu banco
                      db='Prefeitura',
                      cursorclass=pymysql.cursors.DictCursor
                      )


class CidadeListView(generic.ListView):

    template_name = 'tcidades/index2.html'
    context_object_name = 'cidades'
    paginate_by = 5

    def get_queryset(self):
        queryset = Cidade.objects.all()
        q = self.request.GET.get('q', '')

        if q:
            queryset = queryset.filter(
                nameCidade__icontains=q
            )
        return queryset


index = CidadeListView.as_view()
# Função anomalias
def anomalias(request, slug):
    global data_Final
    global data_Inicial

    cidades = get_object_or_404(Cidade, slug=slug)
    listaCidades = Cidade.objects.all()
    contexto = {}

    # ====================================================================================
    # LOGICA PARA FORMULARIOS
    # ====================================================================================
    is_valid = False
    cidade2=None

    # ====================================================================================
    # variaveis para estatiticas
    nomeEstatisticoAdm = valorEstatisticoAdm = listaIndicesAdm=[]
    nomeEstatisticoSaude = valorEstatisticoSaude = listaIndicesSaude=[]
    nomeEstatisticoEducacao = valorEstatisticoEducacao = listaIndicesEducacao=[]
    nomeEstatisticoSeguranca = valorEstatisticoSeguranca = listaIndicesSeguranca=[]
    nomeEstatisticoSaneamento = valorEstatisticoSaneamento = listaIndicesSaneamento=[]
    nomeEstatisticoSocial = valorEstatisticoSocial = listaIndicesSocial=[]
    evolucaoDaMediaAdm = evolucaoDaMediaSaude = evolucaoDaMediaEducacao = []
    evolucaoDaMediaSeguranca = evolucaoDaMediaSaneamento = evolucaoDaMediaSocial = []
    desvioPadraoAdm = mediaAdm = None
    desvioPadraoSaude = mediaSaude = None
    desvioPadraoEducacao = mediaEducacao = None
    desvioPadraoSeguranca = mediaSeguranca = None
    desvioPadraoSaneamento = mediaSaneamento = None
    desvioPadraoSocial = mediaSocial = None
    # ===================================================================================

    # ===================================================================================
    # Codigo para atualização
    if request.method != 'POST':
        print("grafico NPOST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        dados = SearchClasses()

        populacaoTotal = round(
            int(populTotal(con, cidades).replace(".", "")), 2)

        # ===================================================Algoritmo de estatiticas========================================================
        # estatistica adm
        print("teste")
        print("=========================================================================")

        # fim estatistica adm
        listaPorDiaAdm = dados.buscaDiaAdm( con, cidades.idCliente, cidades, data_Inicial, data_Final)
        nomeEstatisticoAdm = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaAdm]
        valorEstatisticoAdm = [float(obj['soma']) for obj in listaPorDiaAdm]
        indice = 0

        media = 0
        somaTotal = 0
        listaDiaSomaAdm = []
        evolucaoDaMediaAdm = []
        while indice < len(valorEstatisticoAdm):
            somaTotal = somaTotal + valorEstatisticoAdm[indice]
            media = round( somaTotal / (indice+1), 2)
            evolucaoDaMediaAdm.append(media)
            indice += + 1

        for x in listaPorDiaAdm:
            listaDiaSomaAdm.append(float(x['soma']))

        if len(listaDiaSomaAdm) >=2:                
            desvioPadraoAdm = statistics.stdev(listaDiaSomaAdm) 
            mediaAdm = statistics.mean(listaDiaSomaAdm)

            incide2=0
            for y in listaPorDiaAdm:
                if y["soma"] > ( mediaAdm + 2*desvioPadraoAdm ):
                    listaIndicesAdm.append(incide2)
                incide2 += +1
        # estatistica Saude
        listaPorDiaSaude = dados.buscaDiaSaude( con, cidades.idCliente, cidades, data_Inicial, data_Final  )
        nomeEstatisticoSaude = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSaude]
        valorEstatisticoSaude = [float(obj['soma']) for obj in listaPorDiaSaude]
        indice = 0

        media = 0
        somaTotal = 0
        listaDiaSomaSaude = []
        evolucaoDaMediaSaude = []
        while indice < len(valorEstatisticoSaude):
            somaTotal = somaTotal + valorEstatisticoSaude[indice]
            media = round( somaTotal / (indice+1), 2)
            evolucaoDaMediaSaude.append(media)
            indice += + 1
        print("valortaotal", somaTotal)
        for x in listaPorDiaSaude:
            listaDiaSomaSaude.append(float(x['soma']))

        if len(listaDiaSomaSaude) >=2:                
            desvioPadraoSaude = statistics.stdev(listaDiaSomaSaude) 
            mediaSaude = statistics.mean(listaDiaSomaSaude)

            incide2=0
            for y in listaPorDiaSaude:
                if y["soma"] > ( mediaSaude + 2*desvioPadraoSaude ):
                    listaIndicesSaude.append(incide2)
                incide2 += +1
        # fim estatistica Saude

        # estatistica Educacao
        listaPorDiaEducacao = dados.buscaDiaEducacao( con, cidades.idCliente, cidades, data_Inicial, data_Final  )
        nomeEstatisticoEducacao = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaEducacao]
        valorEstatisticoEducacao = [float(obj['soma']) for obj in listaPorDiaEducacao]
        indice = 0

        media = 0
        somaTotal = 0
        listaDiaSomaEducacao = []
        evolucaoDaMediaEducacao = []
        while indice < len(valorEstatisticoEducacao):
            somaTotal = somaTotal + valorEstatisticoEducacao[indice]
            media = round( somaTotal / (indice+1), 2)
            evolucaoDaMediaEducacao.append(media)
            indice += + 1

        for x in listaPorDiaEducacao:
            listaDiaSomaEducacao.append(float(x['soma']))

        if len(listaDiaSomaEducacao) >= 2 :
            desvioPadraoEducacao = statistics.stdev(listaDiaSomaEducacao) 
            mediaEducacao = statistics.mean(listaDiaSomaEducacao)

            incide2=0
            for y in listaPorDiaEducacao:
                if y["soma"] > ( mediaEducacao + 2*desvioPadraoEducacao ):
                    listaIndicesEducacao.append(incide2)
                incide2 += +1
        # fim estatistica Educacao

        # estatistica Seguranca
        listaPorDiaSeguranca = dados.buscaDiaSeguranca( con, cidades.idCliente, cidades, data_Inicial, data_Final  )
        nomeEstatisticoSeguranca = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSeguranca]
        valorEstatisticoSeguranca = [float(obj['soma']) for obj in listaPorDiaSeguranca]
        indice = 0

        media = 0
        somaTotal = 0
        listaDiaSomaSeguranca = []
        evolucaoDaMediaSeguranca = []
        while indice < len(valorEstatisticoSeguranca):
            somaTotal = somaTotal + valorEstatisticoSeguranca[indice]
            media = round( somaTotal / (indice+1), 2)
            evolucaoDaMediaSeguranca.append(media)
            indice += + 1

        for x in listaPorDiaSeguranca:
            listaDiaSomaSeguranca.append(float(x['soma']))
    
        if len(listaDiaSomaSeguranca) >= 2 :
            desvioPadraoSeguranca = statistics.stdev(listaDiaSomaSeguranca) 
            mediaSeguranca = statistics.mean(listaDiaSomaSeguranca)

            incide2=0
            for y in listaPorDiaSeguranca:
                if y["soma"] > ( mediaSeguranca + 2*desvioPadraoSeguranca ):
                    listaIndicesSeguranca.append(incide2)
                incide2 += +1
        # fim estatistica Seguranca

        # estatistica Saneamento
        listaPorDiaSaneamento = dados.buscaDiaSaneamento( con, cidades.idCliente, cidades, data_Inicial, data_Final  )
        nomeEstatisticoSaneamento = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSaneamento]
        valorEstatisticoSaneamento = [float(obj['soma']) for obj in listaPorDiaSaneamento]
        indice = 0

        media = 0
        somaTotal = 0
        listaDiaSomaSaneamento = []
        evolucaoDaMediaSaneamento = []
        while indice < len(valorEstatisticoSaneamento):
            somaTotal = somaTotal + valorEstatisticoSaneamento[indice]
            media = round( somaTotal / (indice+1), 2)
            evolucaoDaMediaSaneamento.append(media)
            indice += + 1

        for x in listaPorDiaSaneamento:
            listaDiaSomaSaneamento.append(float(x['soma']))

        if len(listaDiaSomaSaneamento) >= 2 :
            desvioPadraoSaneamento = statistics.stdev(listaDiaSomaSaneamento) 
            mediaSaneamento = statistics.mean(listaDiaSomaSaneamento)

            incide2=0
            for y in listaPorDiaSaneamento:
                if y["soma"] > ( mediaSaneamento + 2*desvioPadraoSaneamento ):
                    listaIndicesSaneamento.append(incide2)
                incide2 += +1
        # fim estatistica Saneamento

        # estatistica Social
        listaPorDiaSocial = dados.buscaDiaSocial( con, cidades.idCliente, cidades, data_Inicial, data_Final  )
        nomeEstatisticoSocial = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSocial]
        valorEstatisticoSocial = [float(obj['soma']) for obj in listaPorDiaSocial]
        indice = 0

        media = 0
        somaTotal = 0
        listaDiaSomaSocial = []
        evolucaoDaMediaSocial = []
        while indice < len(valorEstatisticoSocial):
            somaTotal = somaTotal + valorEstatisticoSocial[indice]
            media = round( somaTotal / (indice+1), 2)
            evolucaoDaMediaSocial.append(media)
            indice += + 1

        for x in listaPorDiaSocial:
            listaDiaSomaSocial.append(float(x['soma']))

        if len(listaDiaSomaSocial) >= 2 :
            desvioPadraoSocial = statistics.stdev(listaDiaSomaSocial) 
            mediaSocial = statistics.mean(listaDiaSomaSocial)

            incide2=0
            for y in listaPorDiaSocial:
                if y["soma"] > ( mediaSocial + 2*desvioPadraoSocial ):
                    listaIndicesSocial.append(incide2)
                incide2 += +1
            
        # fim estatistica Social
        # ===================================================================================================================================

        
        cidade2 = str(cidades)[24:]
        # =========================================================== FIm ====================================================================
    if request.method == 'POST':
        
        print("grafico POST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        form = SearchForm(request.POST)
        if form.is_valid():
            is_valid = True

            data_Final = form.cleaned_data['dataFinal']
            data_Inicial = form.cleaned_data['dataInicial']



            # ===================================================Algoritmo de estatiticas========================================================
            # estatistica adm
            print("teste")
            print("=========================================================================")

            # fim estatistica adm
            listaPorDiaAdm = form.buscaDiaAdm( con, cidades.idCliente, cidades )
            nomeEstatisticoAdm = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaAdm]
            valorEstatisticoAdm = [float(obj['soma']) for obj in listaPorDiaAdm]
            indice = 0

            media = 0
            somaTotal = 0
            listaDiaSomaAdm = []
            evolucaoDaMediaAdm = []
            while indice < len(valorEstatisticoAdm):
                somaTotal = somaTotal + valorEstatisticoAdm[indice]
                media = round( somaTotal / (indice+1), 2)
                # print("anterior", valorEstatisticoAdm[indice] )
                # print("indice",indice," = media", media)
                evolucaoDaMediaAdm.append(media)
                indice += + 1

            for x in listaPorDiaAdm:
                listaDiaSomaAdm.append(float(x['soma']))

            if len(listaDiaSomaAdm) >=2:                
                desvioPadraoAdm = statistics.stdev(listaDiaSomaAdm) 
                mediaAdm = statistics.mean(listaDiaSomaAdm)

                incide2=0
                for y in listaPorDiaAdm:
                    if y["soma"] > ( mediaAdm + 2*desvioPadraoAdm ):
                        listaIndicesAdm.append(incide2)
                    incide2 += +1
            # estatistica Saude
            listaPorDiaSaude = form.buscaDiaSaude( con, cidades.idCliente, cidades )
            nomeEstatisticoSaude = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSaude]
            valorEstatisticoSaude = [float(obj['soma']) for obj in listaPorDiaSaude]
            indice = 0

            media = 0
            somaTotal = 0
            listaDiaSomaSaude = []
            evolucaoDaMediaSaude = []
            while indice < len(valorEstatisticoSaude):
                somaTotal = somaTotal + valorEstatisticoSaude[indice]
                media = round( somaTotal / (indice+1), 2)
                # print("anterior", valorEstatisticoAdm[indice] )
                # print("indice",indice," = media", media)
                evolucaoDaMediaSaude.append(media)
                indice += + 1
            print("somaTotal",somaTotal)

            for x in listaPorDiaSaude:
                listaDiaSomaSaude.append(float(x['soma']))

            if len(listaDiaSomaAdm) >=2:                
                desvioPadraoSaude = statistics.stdev(listaDiaSomaSaude) 
                mediaSaude = statistics.mean(listaDiaSomaSaude)

                incide2=0
                for y in listaPorDiaSaude:
                    if y["soma"] > ( mediaSaude + 2*desvioPadraoSaude ):
                        listaIndicesSaude.append(incide2)
                    incide2 += +1
            # fim estatistica Saude

            # estatistica Educacao
            listaPorDiaEducacao = form.buscaDiaEducacao( con, cidades.idCliente, cidades )
            nomeEstatisticoEducacao = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaEducacao]
            valorEstatisticoEducacao = [float(obj['soma']) for obj in listaPorDiaEducacao]
            indice = 0

            media = 0
            somaTotal = 0
            listaDiaSomaEducacao = []
            evolucaoDaMediaEducacao = []
            while indice < len(valorEstatisticoEducacao):
                somaTotal = somaTotal + valorEstatisticoEducacao[indice]
                media = round( somaTotal / (indice+1), 2)
                evolucaoDaMediaEducacao.append(media)
                indice += + 1

            for x in listaPorDiaEducacao:
                listaDiaSomaEducacao.append(float(x['soma']))

            if len(listaDiaSomaEducacao) >= 2 :
                desvioPadraoEducacao = statistics.stdev(listaDiaSomaEducacao) 
                mediaEducacao = statistics.mean(listaDiaSomaEducacao)

                incide2=0
                for y in listaPorDiaEducacao:
                    if y["soma"] > ( mediaEducacao + 2*desvioPadraoEducacao ):
                        listaIndicesEducacao.append(incide2)
                    incide2 += +1
            # fim estatistica Educacao

            # estatistica Seguranca
            listaPorDiaSeguranca = form.buscaDiaSeguranca( con, cidades.idCliente, cidades )
            nomeEstatisticoSeguranca = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSeguranca]
            valorEstatisticoSeguranca = [float(obj['soma']) for obj in listaPorDiaSeguranca]
            indice = 0

            media = 0
            somaTotal = 0
            listaDiaSomaSeguranca = []
            evolucaoDaMediaSeguranca = []
            while indice < len(valorEstatisticoSeguranca):
                somaTotal = somaTotal + valorEstatisticoSeguranca[indice]
                media = round( somaTotal / (indice+1), 2)
                evolucaoDaMediaSeguranca.append(media)
                indice += + 1

            for x in listaPorDiaSeguranca:
                listaDiaSomaSeguranca.append(float(x['soma']))
        
            if len(listaDiaSomaSeguranca) >= 2 :
                desvioPadraoSeguranca = statistics.stdev(listaDiaSomaSeguranca) 
                mediaSeguranca = statistics.mean(listaDiaSomaSeguranca)

                incide2=0
                for y in listaPorDiaSeguranca:
                    if y["soma"] > ( mediaSeguranca + 2*desvioPadraoSeguranca ):
                        listaIndicesSeguranca.append(incide2)
                    incide2 += +1
            # fim estatistica Seguranca

            # estatistica Saneamento
            listaPorDiaSaneamento = form.buscaDiaSaneamento( con, cidades.idCliente, cidades )
            nomeEstatisticoSaneamento = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSaneamento]
            valorEstatisticoSaneamento = [float(obj['soma']) for obj in listaPorDiaSaneamento]
            indice = 0

            media = 0
            somaTotal = 0
            listaDiaSomaSaneamento = []
            evolucaoDaMediaSaneamento = []
            while indice < len(valorEstatisticoSaneamento):
                somaTotal = somaTotal + valorEstatisticoSaneamento[indice]
                media = round( somaTotal / (indice+1), 2)
                evolucaoDaMediaSaneamento.append(media)
                indice += + 1

            for x in listaPorDiaSaneamento:
                listaDiaSomaSaneamento.append(float(x['soma']))

            if len(listaDiaSomaSaneamento) >= 2 :
                desvioPadraoSaneamento = statistics.stdev(listaDiaSomaSaneamento) 
                mediaSaneamento = statistics.mean(listaDiaSomaSaneamento)

                incide2=0
                for y in listaPorDiaSaneamento:
                    if y["soma"] > ( mediaSaneamento + 2*desvioPadraoSaneamento ):
                        listaIndicesSaneamento.append(incide2)
                    incide2 += +1
            # fim estatistica Saneamento

            # estatistica Social
            listaPorDiaSocial = form.buscaDiaSocial( con, cidades.idCliente, cidades )
            nomeEstatisticoSocial = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaSocial]
            valorEstatisticoSocial = [float(obj['soma']) for obj in listaPorDiaSocial]
            indice = 0

            media = 0
            somaTotal = 0
            listaDiaSomaSocial = []
            evolucaoDaMediaSocial = []
            while indice < len(valorEstatisticoSocial):
                somaTotal = somaTotal + valorEstatisticoSocial[indice]
                media = round( somaTotal / (indice+1), 2)
                evolucaoDaMediaSocial.append(media)
                indice += + 1

            for x in listaPorDiaSocial:
                listaDiaSomaSocial.append(float(x['soma']))

            if len(listaDiaSomaSocial) >= 2 :
                desvioPadraoSocial = statistics.stdev(listaDiaSomaSocial) 
                mediaSocial = statistics.mean(listaDiaSomaSocial)

                incide2=0
                for y in listaPorDiaSocial:
                    if y["soma"] > ( mediaSocial + 2*desvioPadraoSocial ):
                        listaIndicesSocial.append(incide2)
                    incide2 += +1
                
            # fim estatistica Social
            # ===================================================================================================================================


            populacaoTotal = round(
                int(populTotal(con, cidades).replace(".", "")), 2)
            # ==============fimConversoes======================
            # limpa formulario
        form = SearchForm(None)
    else:
        form = SearchForm()


    contexto = {
        'cidade': cidades,
        'id': cidades.idCliente,
        'form': form,
        'is_valid': is_valid,
        'populacaoTotal': populacaoTotal,
        'dataFinal': data_Final,
        'dataInicial': data_Inicial,
        'cidade2': cidade2,

        'nomeEstatisticoAdm': json.dumps(nomeEstatisticoAdm),
        'valorEstatisticoAdm': json.dumps(valorEstatisticoAdm),
        'desvioPadraoAdm': desvioPadraoAdm,
        'mediaAdm': mediaAdm,
        'listaIndicesAdm':json.dumps(listaIndicesAdm),

        'nomeEstatisticoSaude': json.dumps(nomeEstatisticoSaude),
        'valorEstatisticoSaude': json.dumps(valorEstatisticoSaude),
        'desvioPadraoSaude': desvioPadraoSaude,
        'mediaSaude': mediaSaude,
        'listaIndicesSaude':json.dumps(listaIndicesSaude),
        
        'nomeEstatisticoEducacao': json.dumps(nomeEstatisticoEducacao),
        'valorEstatisticoEducacao': json.dumps(valorEstatisticoEducacao),
        'desvioPadraoEducacao': desvioPadraoEducacao,
        'mediaEducacao': mediaEducacao,
        'listaIndicesEducacao':json.dumps(listaIndicesEducacao),

        'nomeEstatisticoSeguranca': json.dumps(nomeEstatisticoSeguranca),
        'valorEstatisticoSeguranca': json.dumps(valorEstatisticoSeguranca),
        'desvioPadraoSeguranca': desvioPadraoSeguranca,
        'mediaSeguranca': mediaSeguranca,
        'listaIndicesSeguranca':json.dumps(listaIndicesSeguranca),

        'nomeEstatisticoSaneamento': json.dumps(nomeEstatisticoSaneamento),
        'valorEstatisticoSaneamento': json.dumps(valorEstatisticoSaneamento),
        'desvioPadraoSaneamento': desvioPadraoSaneamento,
        'mediaSaneamento': mediaSaneamento,
        'listaIndicesSaneamento':json.dumps(listaIndicesSaneamento),

        'nomeEstatisticoSocial': json.dumps(nomeEstatisticoSocial),
        'valorEstatisticoSocial': json.dumps(valorEstatisticoSocial),
        'desvioPadraoSocial': desvioPadraoSocial,
        'mediaSocial': mediaSocial,
        'listaIndicesSocial':json.dumps(listaIndicesSocial),

        'evolucaoDaMediaAdm': evolucaoDaMediaAdm,
        'evolucaoDaMediaSaude': evolucaoDaMediaSaude ,
        'evolucaoDaMediaSocial': evolucaoDaMediaSocial,
        'evolucaoDaMediaSaneamento': evolucaoDaMediaSaneamento,
        'evolucaoDaMediaSeguranca': evolucaoDaMediaSeguranca,
        'evolucaoDaMediaEducacao': evolucaoDaMediaEducacao,
        'evolucaoDaMediaSaude': evolucaoDaMediaSaude
    }

    try:
        template_name = 'tInform/anomaly.html'
        return render(request, template_name, contexto)
    except Cidade.DoesNotExist:
        raise Http404
# Fim anomalias

def grafico(request, slug):
    global data_Final
    global data_Inicial

    cidades = get_object_or_404(Cidade, slug=slug)
    listaCidades = Cidade.objects.all()
    contexto = {}

    # ================================================
    # LOGICA PARA FORMULARIOS
    # ================================================
    is_valid = False
    # data_Final = None
    # data_Inicial = None
    # LOGICA PARA FORMULARIOS
    llistaOrgao = llistaElemento = llistaSubFuncao = llistaFuncao = llistaProjeto = llistaDiarias = None
     # conversoes para JASON
    nomeOrgao = valorOrgao =  nomeElemento = valorElemento =  nomeFuncao = valorFuncao =  nomeSubFuncao = valorSubFuncao =  nomeProjeto = valorProjeto =  nomeDiarias = valorDiarias =  nomeSaudePopul = valorSaudePopul = nomeEducacaoPopul = valorEducacaoPopul = valorAdminPopul = nomeAdminPopul = populacaoTotal = listaDicFuncoes = None
    # =================variaveis para as medias======================
    n_posMinSaude = n_posMaxSaude = n_minSaude = n_maxSaude = None
    n_posMinAdmin = n_posMaxAdmin = n_minAdmin = n_maxAdmin = None
    n_posMinEducacao = n_posMaxEducacao = n_minEducacao = n_maxEducacao = None

    encEspeciaisLista = dirCidadaniaLista = municipiosLista = cidade2 =  None
    mediaSaudeLista = mediaEducacaoLista = mediaAdmLista = []
    # ids nao podem serem declarado em uma linha apenas
    idClienteValorSaude = []
    idClienteValorEducacao = []
    idClienteValorAdm = []
    mediaSaudeLista_labels = mediaEducacaoLista_labels = mediaAdminLista_labe = []
    mediaEducacaoLista_valor =   mediaSaudeLista_valor = mediaAdminLista_valor = []
    # ===============================================================

    # ==============fimConversoes====================================
    if request.method != 'POST':
        print("grafico NPOST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        dados = SearchClasses()

        a1 = dados.buscaSaudePorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        a2 = dados.buscaEducacaoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        a3 = dados.buscaAdministracaoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)

        llistaOrgao = dados.buscaDadosOrgao(
            con, cidades.idCliente, data_Inicial, data_Final)
        llistaElemento = dados.buscaDadosElemento(
            con, cidades.idCliente, data_Inicial, data_Final)
        llistaFuncao = dados.buscaDadosFuncao(
            con, cidades.idCliente, data_Inicial, data_Final)
        llistaSubFuncao = dados.buscaDadosSubFuncao(
            con, cidades.idCliente, data_Inicial, data_Final)
        llistaProjeto = dados.buscaDadosProjeto(
            con, cidades.idCliente, data_Inicial, data_Final)
        llistaDiarias = dados.buscaDadosDiarias(
            con, cidades.idCliente, data_Inicial, data_Final)

        nomeOrgao = [obj['divisao'] for obj in llistaOrgao]
        valorOrgao = [float(obj['soma']) for obj in llistaOrgao]

        nomeElemento = [obj['divisao'] for obj in llistaElemento]
        valorElemento = [float(obj['soma']) for obj in llistaElemento]

        nomeFuncao = [obj['divisao'] for obj in llistaFuncao]
        valorFuncao = [float(obj['soma']) for obj in llistaFuncao]

        nomeSubFuncao = [obj['divisao'] for obj in llistaSubFuncao]
        valorSubFuncao = [float(obj['soma']) for obj in llistaSubFuncao]

        nomeProjeto = [obj['divisao'] for obj in llistaProjeto[0:20]]
        valorProjeto = [float(obj['soma']) for obj in llistaProjeto[0:20]]

        nomeDiarias = [obj['Nome'] for obj in llistaDiarias[0:20]]
        valorDiarias = [float(obj['soma']) for obj in llistaDiarias[0:20]]

        nomeSaudePopul = [obj['divisao'] for obj in a1]
        valorSaudePopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                           for obj in a1]
        # print(valorSaudePopul)
        nomeEducacaoPopul = [obj['divisao'] for obj in a2]
        valorEducacaoPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                              for obj in a2]
        # print(valorEducacaoPopul)
        nomeAdminPopul = [obj['divisao'] for obj in a3]
        valorAdminPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                           for obj in a3]

        populacaoTotal = round(
            int(populTotal(con, cidades).replace(".", "")), 2)


        # ===================================================== Algoritmo de media ===========================================================
        listaDicFuncoes = dados.retornaFuncaoPorPopul(con,data_Inicial,data_Final)
        nomeIDclientePopul = listaDasCidades(con)

        for x in listaDicFuncoes:
            indice=0

            while indice < len(x["listaFuncoes"]):
                if (x["listaFuncoes"][indice]["divisao"]).upper() == "10 - SAUDE":
                    idClienteValorSaude.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

                if (x["listaFuncoes"][indice]["divisao"]).upper() == "04 - ADMINISTRACAO":
                    idClienteValorAdm.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

                if (x["listaFuncoes"][indice]["divisao"]).upper() == "12 - EDUCACAO":
                    idClienteValorEducacao.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

                indice += + 1


        idNomePopul_listaSaude = []
        for n in idClienteValorSaude:
            for m in nomeIDclientePopul:
                if n["idCliente"] == m["idCliente"]: 
                    idNomePopul_listaSaude.append( { "idCliente": n["idCliente"], "nome": m["nome"], "media": round( ( float(n["valor"] ) / int( m["populacao"].replace(".", "")) ), 2) } )   

        mediaSaudeLista_labels = [obj['nome'][24:] for obj in idNomePopul_listaSaude]
        mediaSaudeLista_valor = [obj['media'] for obj in idNomePopul_listaSaude]

        if len(mediaSaudeLista_valor) != 0:
            n_minSaude = min(mediaSaudeLista_valor)
            n_posMinSaude = mediaSaudeLista_valor.index(n_minSaude)
            n_maxSaude = max(mediaSaudeLista_valor)
            n_posMaxSaude = mediaSaudeLista_valor.index(n_maxSaude)

        idNomePopul_listaEducacao = []
        for n in idClienteValorEducacao:
            for m in nomeIDclientePopul:
                if n["idCliente"] == m["idCliente"]: 
                    idNomePopul_listaEducacao.append( { "idCliente": n["idCliente"], "nome": m["nome"], "media": round( ( float(n["valor"] ) / int( m["populacao"].replace(".", "")) ), 2) } )   

        mediaEducacaoLista_labels = [obj['nome'][24:] for obj in idNomePopul_listaEducacao]
        mediaEducacaoLista_valor = [obj['media'] for obj in idNomePopul_listaEducacao]
        if len(mediaEducacaoLista_valor) !=0 :
            n_minEducacao = min(mediaEducacaoLista_valor)
            n_posMinEducacao = mediaEducacaoLista_valor.index(n_minEducacao)
            n_maxEducacao = max(mediaEducacaoLista_valor)
            n_posMaxEducacao = mediaEducacaoLista_valor.index(n_maxEducacao)

        idNomePopul_listaAdm = []
        for n in idClienteValorAdm:
            for m in nomeIDclientePopul:
                if n["idCliente"] == m["idCliente"]: 
                    idNomePopul_listaAdm.append( { "idCliente": n["idCliente"], "nome": m["nome"], "media": round( ( float(n["valor"] ) / int( m["populacao"].replace(".", "")) ), 2) } )   

        mediaAdminLista_labels = [obj['nome'][24:] for obj in idNomePopul_listaAdm]
        mediaAdminLista_valor = [obj['media'] for obj in idNomePopul_listaAdm]

        if len(mediaAdminLista_valor) !=0 :
            n_minAdmin = min(mediaAdminLista_valor)
            n_posMinAdmin = mediaAdminLista_valor.index(n_minAdmin)
            n_maxAdmin = max(mediaAdminLista_valor)
            n_posMaxAdmin = mediaAdminLista_valor.index(n_maxAdmin)
        
        cidade2 = str(cidades)[24:]
        # =========================================================== Fim ====================================================================
    if request.method == 'POST':
        print("grafico POST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        form = SearchForm(request.POST)
        if form.is_valid():
            is_valid = True

            data_Final = form.cleaned_data['dataFinal']
            data_Inicial = form.cleaned_data['dataInicial']

            a1 = form.buscaSaudePorData(con, cidades.idCliente)
            a2 = form.buscaEducacaoPorData(con, cidades.idCliente)
            a3 = form.buscaAdministracaoPorData(
                con, cidades.idCliente)

            llistaOrgao = form.buscaDadosOrgao(con, cidades.idCliente)
            llistaElemento = form.buscaDadosElemento(con, cidades.idCliente)
            llistaFuncao = form.buscaDadosFuncao(con, cidades.idCliente)
            llistaSubFuncao = form.buscaDadosSubFuncao(con, cidades.idCliente)
            llistaProjeto = form.buscaDadosProjeto(con, cidades.idCliente)
            lista_saudePopul = form.buscaSaudePorPopul( con, cidades.idCliente, cidades)
            lista_educacaoPopul = form.buscaEducacaoPopul( con, cidades.idCliente, cidades)
            lista_adminPopul = form.buscaAdministracaoPopul( con, cidades.idCliente, cidades)
            llistaDiarias = form.buscaDadosDiarias(con, cidades.idCliente)
            label = form.buscaSaudePorData(con, cidades.idCliente)

            # ===================================================Algoritmo de estatiticas========================================================
            # estatistica adm
            listaDiaSomaAdm = []
            listaPorDiaAdm = form.buscaDiaAdm( con, cidades.idCliente, cidades )
            nomeEstatisticoAdm = [str(obj['ano'])+":"+str(obj['semana']) for obj in listaPorDiaAdm]
            valorEstatisticoAdm = [float(obj['soma']) for obj in listaPorDiaAdm]

            for x in listaPorDiaAdm:
                print(x)
                listaDiaSomaAdm.append(float(x['soma']))

            print("desvio padrao", statistics.stdev(listaDiaSomaAdm) )
            desvioPadraoAdm = statistics.stdev(listaDiaSomaAdm) 
            print("media", statistics.mean(listaDiaSomaAdm) )
            mediaAdm = statistics.mean(listaDiaSomaAdm) 


            # ===================================================================================================================================

            dicDeFuncoes = form.retornaListaFuncoes(con, cidades.idCliente)
            listaDeFuncoes = [obj['divisao'] for obj in dicDeFuncoes]
            listaDicFuncoes = form.retornaDicFuncoes(con, cidades.idCliente, listaDeFuncoes)

            # ===================================================== Algoritmo de media entre cidades ===========================================================
            listaDicFuncoes = form.retornaFuncaoPorPopul(con)
            nomeIDclientePopul = listaDasCidades(con)

            for x in listaDicFuncoes:
                indice=0

                while indice < len(x["listaFuncoes"]):
                    if (x["listaFuncoes"][indice]["divisao"]).upper() == "10 - SAUDE":
                        idClienteValorSaude.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

                    if (x["listaFuncoes"][indice]["divisao"]).upper() == "04 - ADMINISTRACAO":
                        idClienteValorAdm.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

                    if (x["listaFuncoes"][indice]["divisao"]).upper() == "12 - EDUCACAO":
                        idClienteValorEducacao.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

                    indice += + 1


            idNomePopul_listaSaude = []
            for n in idClienteValorSaude:
                for m in nomeIDclientePopul:
                    if n["idCliente"] == m["idCliente"]: 
                        idNomePopul_listaSaude.append( { "idCliente": n["idCliente"], "nome": m["nome"], "media": round( ( float(n["valor"] ) / int( m["populacao"].replace(".", "")) ), 2) } )   

            mediaSaudeLista_labels = [obj['nome'][24:] for obj in idNomePopul_listaSaude]
            mediaSaudeLista_valor = [obj['media'] for obj in idNomePopul_listaSaude]

            n_minSaude = min(mediaSaudeLista_valor)
            n_posMinSaude = mediaSaudeLista_valor.index(n_minSaude)
            n_maxSaude = max(mediaSaudeLista_valor)
            n_posMaxSaude = mediaSaudeLista_valor.index(n_maxSaude)
            idNomePopul_listaEducacao = []

            for n in idClienteValorEducacao:
                for m in nomeIDclientePopul:
                    if n["idCliente"] == m["idCliente"]: 
                        idNomePopul_listaEducacao.append( { "idCliente": n["idCliente"], "nome": m["nome"], "media": round( ( float(n["valor"] ) / int( m["populacao"].replace(".", "")) ), 2) } )   

            mediaEducacaoLista_labels = [obj['nome'][24:] for obj in idNomePopul_listaEducacao]
            mediaEducacaoLista_valor = [obj['media'] for obj in idNomePopul_listaEducacao]

            cidade2 = str(cidades)[24:]


            n_minEducacao = min(mediaEducacaoLista_valor)
            n_posMinEducacao = mediaEducacaoLista_valor.index(n_minEducacao)
            n_maxEducacao = max(mediaEducacaoLista_valor)
            n_posMaxEducacao = mediaEducacaoLista_valor.index(n_maxEducacao)

            idNomePopul_listaAdm = []
            for n in idClienteValorAdm:
                for m in nomeIDclientePopul:
                    if n["idCliente"] == m["idCliente"]: 
                        idNomePopul_listaAdm.append( { "idCliente": n["idCliente"], "nome": m["nome"], "media": round( ( float(n["valor"] ) / int( m["populacao"].replace(".", "")) ), 2) } )   

            mediaAdminLista_labels = [obj['nome'][24:] for obj in idNomePopul_listaAdm]
            mediaAdminLista_valor = [obj['media'] for obj in idNomePopul_listaAdm]

            n_minAdmin = min(mediaAdminLista_valor)
            n_posMinAdmin = mediaAdminLista_valor.index(n_minAdmin)
            n_maxAdmin = max(mediaAdminLista_valor)
            n_posMaxAdmin = mediaAdminLista_valor.index(n_maxAdmin)

            # =========================================================== Fim ====================================================================


            nomeOrgao = [obj['divisao'] for obj in llistaOrgao]
            valorOrgao = [float(obj['soma']) for obj in llistaOrgao]

            nomeElemento = [obj['divisao'] for obj in llistaElemento]
            valorElemento = [float(obj['soma']) for obj in llistaElemento]

            nomeFuncao = [obj['divisao'] for obj in llistaFuncao]
            valorFuncao = [float(obj['soma']) for obj in llistaFuncao]

            nomeSubFuncao = [obj['divisao'] for obj in llistaSubFuncao]
            valorSubFuncao = [float(obj['soma']) for obj in llistaSubFuncao]

            nomeProjeto = [obj['divisao'] for obj in llistaProjeto[0:20]]
            valorProjeto = [float(obj['soma']) for obj in llistaProjeto[0:20]]

            nomeDiarias = [obj['Nome'] for obj in llistaDiarias[0:20]]
            valorDiarias = [float(obj['soma']) for obj in llistaDiarias[0:20]]

            nomeSaudePopul = [obj['divisao'] for obj in a1]
            valorSaudePopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                               for obj in a1]
            # print(valorSaudePopul)
            nomeEducacaoPopul = [obj['divisao'] for obj in a2]
            valorEducacaoPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                                  for obj in a2]
            # print(valorEducacaoPopul)
            nomeAdminPopul = [obj['divisao'] for obj in a3]
            valorAdminPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                               for obj in a3]

            populacaoTotal = round(
                int(populTotal(con, cidades).replace(".", "")), 2)
            # ==============fimConversoes======================
            # limpa formulario
        form = SearchForm(None)
    else:
        form = SearchForm()


    # print(valorFuncao)

    contexto = {
        'cidade': cidades,
        'id': cidades.idCliente,
        'form': form,
        'is_valid': is_valid,
        'populacaoTotal': populacaoTotal,
        'dataFinal': data_Final,
        'dataInicial': data_Inicial,

        'nomeOrgao': json.dumps(nomeOrgao),
        'valorOrgao': json.dumps(valorOrgao),

        'nomeFuncao': json.dumps(nomeFuncao),
        'valorFuncao': json.dumps(valorFuncao),

        'nomeElemento': json.dumps(nomeElemento),
        'valorElemento': json.dumps(valorElemento),

        'nomeSubFuncao': json.dumps(nomeSubFuncao),
        'valorSubFuncao': json.dumps(valorSubFuncao),

        'nomeProjeto': json.dumps(nomeProjeto),
        'valorProjeto': json.dumps(valorProjeto),

        'nomeDiarias': json.dumps(nomeDiarias),
        'valorDiarias': json.dumps(valorDiarias),

        'nomeSaudePopul': json.dumps(nomeSaudePopul),
        'valorSaudePopul': json.dumps(valorSaudePopul),

        'nomeEducacaoPopul': json.dumps(nomeEducacaoPopul),
        'valorEducacaoPopul': json.dumps(valorEducacaoPopul),

        'nomeAdminPopul': json.dumps(nomeAdminPopul),
        'valorAdminPopul': json.dumps(valorAdminPopul),

        'cidade2': cidade2,

        'n_minSaude': n_minSaude,
        'n_posMinSaude': n_posMinSaude,
        'n_maxSaude': n_maxSaude,
        'n_posMaxSaude': n_posMaxSaude,
        'mediaSaudeLista_labels': json.dumps(mediaSaudeLista_labels),
        'mediaSaudeLista_valor': json.dumps(mediaSaudeLista_valor),

        'n_minEducacao': n_minEducacao,
        'n_posMinEducacao': n_posMinEducacao,
        'n_maxEducacao': n_maxEducacao,
        'n_posMaxEducacao': n_posMaxEducacao,
        'mediaEducacaoLista_labels': json.dumps(mediaEducacaoLista_labels),
        'mediaEducacaoLista_valor': json.dumps(mediaEducacaoLista_valor),

        'n_minAdmin': n_minAdmin,
        'n_posMinAdmin': n_posMinAdmin,
        'n_maxAdmin': n_maxAdmin,
        'n_posMaxAdmin': n_posMaxAdmin,
        'mediaAdminLista_labels': json.dumps(mediaAdminLista_labels),
        'mediaAdminLista_valor': json.dumps(mediaAdminLista_valor),
    }

    try:
        template_name = 'tInform/charts.html'
        return render(request, template_name, contexto)
    except Cidade.DoesNotExist:
        raise Http404


def detalhado(request, slug):
    global data_Final
    global data_Inicial

    cidades = get_object_or_404(Cidade, slug=slug)
    contexto = {}

    is_valid = False
    cidade2=None
    
    lllistaOrgao = educacaoLista = adminitracaoLista = gestaoAmbLista = segurancaLista = culturaLista = socialLista = saneamentoLista = agriculturaLista = transportesLista = urbanismoLista = encEspeciaisLista = dirCidadaniaLista = municipiosLista = None
    # ============================================
    # conversoes para JASON
    nomeOrgao = valorOrgao = nomeEducacao = valorEducacao = nomeAdmin = valorAdmin = nomeGestAmb = valorGestAmb = nomeSeguranca = valorSeguranca = nomeCultura = valorCultura = nomeAssSocial = valorAssSocial = nomeSaneamento = valorSaneamento = nomeAgricultura = valorAgricultura = nomeTransportes = valorTransportes = nomeUrbanismo = valorUrbanismo = nomeEncEspeciais = valorEncEspeciais = nomeDirCidadania = valorDirCidadania = listaDeFuncoes = dicDeFuncoes = listaDicFuncoes = None
    mediaSaudeLista_labels = []
    mediaSaudeLista_valor = []

    idClienteValorAdm= []
    idClienteValorSaude=[]
    idClienteValorEducacao=[]
    # ==============fimConversoes==================

    # TODO:
    # populacao para as cidades

    # with con.cursor() as cursor:
    #     cursor.execute(
    #         "SELECT NOME_MUNICIPIO, POPULACAO FROM Prefeitura2.Populacao")  # noqa E501
    # municipiosLista = cursor.fetchall()
    # print("===================================")
    # for m in municipiosLista:
    #     if str(m['NOME_MUNICIPIO']) in str(cidades):
    #         print(m['NOME_MUNICIPIO'])
    #         quantPopul = m['POPULACAO']
    #         print(quantPopul)
    # print("===================================")
    # print(cidades)
    # print(municipiosLista[0]["NOME_MUNICIPIO"])
    # =============================================
    # codigo para formulario
    # ==================================================================================================
    if request.method != 'POST':
        dados = SearchClasses()
        print("detalhado NPOST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        # dicDeFuncoes = dados.retornaListaFuncoes(con, cidades.idCliente, data_Inicial, data_Final)
        # listaDeFuncoes = [obj['divisao'] for obj in dicDeFuncoes]
        # listaDicFuncoes = dados.retornaDicFuncoes(con, cidades.idCliente, data_Inicial, data_Final, listaDeFuncoes)
        a1 = dados.buscaSaudePorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        a2 = dados.buscaEducacaoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        a3 = dados.buscaAdministracaoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)

        lllistaOrgao = dados.buscaSaudePorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        educacaoLista = dados.buscaEducacaoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        adminitracaoLista = dados.buscaAdministracaoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        gestaoAmbLista = dados.buscaGestaoAmbPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        segurancaLista = dados.buscaSegurancaPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        culturaLista = dados.buscaCulturaPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        socialLista = dados.buscaAssSocialPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        saneamentoLista = dados.buscaSaneamentoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        agriculturaLista = dados.buscaAgriculturaPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        transportesLista = dados.buscaTransportesPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        urbanismoLista = dados.buscaUrbanismoPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        dirCidadaniaLista = dados.buscaDirCidadaniaPorData(
            con, cidades.idCliente, data_Inicial, data_Final)
        encEspeciaisLista = dados.buscaDirCidadaniaPorData(
            con, cidades.idCliente, data_Inicial, data_Final)

        # conversoes para JASON
        nomeOrgao = [obj['divisao'] for obj in lllistaOrgao]
        valorOrgao = [float(obj['soma']) for obj in lllistaOrgao]
        # print("=============orgao================")
        nomeEducacao = [obj['divisao'] for obj in educacaoLista]
        valorEducacao = [float(obj['soma']) for obj in educacaoLista]

        nomeAdmin = [obj['divisao'] for obj in adminitracaoLista]
        valorAdmin = [float(obj['soma']) for obj in adminitracaoLista]
        # print(valorAdmin)
        nomeGestAmb = [obj['divisao'] for obj in gestaoAmbLista]
        valorGestAmb = [float(obj['soma']) for obj in gestaoAmbLista]

        nomeSeguranca = [obj['divisao'] for obj in segurancaLista]
        valorSeguranca = [float(obj['soma']) for obj in segurancaLista]

        nomeCultura = [obj['divisao'] for obj in culturaLista]
        valorCultura = [float(obj['soma']) for obj in culturaLista]

        nomeAssSocial = [obj['divisao'] for obj in socialLista]
        valorAssSocial = [float(obj['soma']) for obj in socialLista]

        nomeSaneamento = [obj['divisao'] for obj in saneamentoLista]
        valorSaneamento = [float(obj['soma']) for obj in saneamentoLista]

        nomeAgricultura = [obj['divisao'] for obj in agriculturaLista]
        valorAgricultura = [float(obj['soma']) for obj in agriculturaLista]

        nomeTransportes = [obj['divisao'] for obj in transportesLista]
        valorTransportes = [float(obj['soma']) for obj in transportesLista]

        nomeUrbanismo = [obj['divisao'] for obj in urbanismoLista]
        valorUrbanismo = [float(obj['soma']) for obj in urbanismoLista]

        nomeEncEspeciais = [obj['divisao'] for obj in encEspeciaisLista]
        valorEncEspeciais = [float(obj['soma'])
                             for obj in encEspeciaisLista]

        nomeDirCidadania = [obj['divisao'] for obj in dirCidadaniaLista]
        valorDirCidadania = [float(obj['soma'])
                             for obj in dirCidadaniaLista]


        nomeSaudePopul = [obj['divisao'] for obj in a1]
        valorSaudePopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                           for obj in a1]
        # print(valorSaudePopul)
        nomeEducacaoPopul = [obj['divisao'] for obj in a2]
        valorEducacaoPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                              for obj in a2]
        # print(valorEducacaoPopul)
        nomeAdminPopul = [obj['divisao'] for obj in a3]
        valorAdminPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                           for obj in a3]

        populacaoTotal = round(
            int(populTotal(con, cidades).replace(".", "")), 2)


    if request.method == 'POST':
        print("detalhado POST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        form = SearchForm(request.POST)
        if form.is_valid():
            is_valid = True

            data_Final = form.cleaned_data['dataFinal']
            data_Inicial = form.cleaned_data['dataInicial']

            # pegar a lista de funções
            a1 = form.buscaSaudePorData(con, cidades.idCliente)
            a2 = form.buscaEducacaoPorData(con, cidades.idCliente)
            a3 = form.buscaAdministracaoPorData(con, cidades.idCliente)


            dicDeFuncoes = form.retornaListaFuncoes(con, cidades.idCliente)
            listaDeFuncoes = [obj['divisao'] for obj in dicDeFuncoes]
            listaDicFuncoes = form.retornaDicFuncoes(
                con, cidades.idCliente, listaDeFuncoes)
            
            lllistaOrgao = form.buscaSaudePorData(con, cidades.idCliente)
            educacaoLista = form.buscaEducacaoPorData(con, cidades.idCliente)
            adminitracaoLista = form.buscaAdministracaoPorData(
                con, cidades.idCliente)
            gestaoAmbLista = form.buscaGestaoAmbPorData(con, cidades.idCliente)
            segurancaLista = form.buscaSegurancaPorData(con, cidades.idCliente)
            culturaLista = form.buscaCulturaPorData(con, cidades.idCliente)
            socialLista = form.buscaAssSocialPorData(con, cidades.idCliente)
            saneamentoLista = form.buscaSaneamentoPorData(
                con, cidades.idCliente)
            agriculturaLista = form.buscaAgriculturaPorData(
                con, cidades.idCliente)
            transportesLista = form.buscaTransportesPorData(
                con, cidades.idCliente)
            urbanismoLista = form.buscaUrbanismoPorData(con, cidades.idCliente)
            dirCidadaniaLista = form.buscaDirCidadaniaPorData(
                con, cidades.idCliente)
            encEspeciaisLista = form.buscaDirCidadaniaPorData(
                con, cidades.idCliente)

            # conversoes para JASON
            nomeOrgao = [obj['divisao'] for obj in lllistaOrgao]
            valorOrgao = [float(obj['soma']) for obj in lllistaOrgao]
            # print("=============orgao================")
            nomeEducacao = [obj['divisao'] for obj in educacaoLista]
            valorEducacao = [float(obj['soma']) for obj in educacaoLista]

            nomeAdmin = [obj['divisao'] for obj in adminitracaoLista]
            valorAdmin = [float(obj['soma']) for obj in adminitracaoLista]
            
            nomeGestAmb = [obj['divisao'] for obj in gestaoAmbLista]
            valorGestAmb = [float(obj['soma']) for obj in gestaoAmbLista]

            nomeSeguranca = [obj['divisao'] for obj in segurancaLista]
            valorSeguranca = [float(obj['soma']) for obj in segurancaLista]

            nomeCultura = [obj['divisao'] for obj in culturaLista]
            valorCultura = [float(obj['soma']) for obj in culturaLista]

            nomeAssSocial = [obj['divisao'] for obj in socialLista]
            valorAssSocial = [float(obj['soma']) for obj in socialLista]

            nomeSaneamento = [obj['divisao'] for obj in saneamentoLista]
            valorSaneamento = [float(obj['soma']) for obj in saneamentoLista]

            nomeAgricultura = [obj['divisao'] for obj in agriculturaLista]
            valorAgricultura = [float(obj['soma']) for obj in agriculturaLista]

            nomeTransportes = [obj['divisao'] for obj in transportesLista]
            valorTransportes = [float(obj['soma']) for obj in transportesLista]

            nomeUrbanismo = [obj['divisao'] for obj in urbanismoLista]
            valorUrbanismo = [float(obj['soma']) for obj in urbanismoLista]

            nomeEncEspeciais = [obj['divisao'] for obj in encEspeciaisLista]
            valorEncEspeciais = [float(obj['soma'])
                                 for obj in encEspeciaisLista]

            nomeDirCidadania = [obj['divisao'] for obj in dirCidadaniaLista]
            valorDirCidadania = [float(obj['soma'])
                                 for obj in dirCidadaniaLista]

            nomeSaudePopul = [obj['divisao'] for obj in a1]
            valorSaudePopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                               for obj in a1]
            nomeEducacaoPopul = [obj['divisao'] for obj in a2]
            valorEducacaoPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                                  for obj in a2]
            nomeAdminPopul = [obj['divisao'] for obj in a3]
            valorAdminPopul = [round(float(obj['soma']) / int(populTotal(con, cidades).replace(".", "")), 2)
                               for obj in a3]

            populacaoTotal = round( int(populTotal(con, cidades).replace(".", "")), 2)

            # limpa formulario
            # form = SearchForm(None)
    else:
        form = SearchForm()
    
    cidade2 = str(cidades)[24:]
    # print("cidade2:", cidade2)
    contexto = {
        'cidade': cidades,
        # 'nomeCidade': cid,
        'id': cidades.idCliente,
        'form': form,
        'is_valid': is_valid,
        'listaDicFuncoes': listaDicFuncoes,
        'populacaoTotal' : populacaoTotal,

        'dataFinal': data_Final,
        'dataInicial': data_Inicial,

        'nomeSaude': json.dumps(nomeOrgao),
        'valorSaude': json.dumps(valorOrgao),

        'nomeEducacao': json.dumps(nomeEducacao),
        'valorEducacao': json.dumps(valorEducacao),

        'nomeAdmin': json.dumps(nomeAdmin),
        'valorAdmin': json.dumps(valorAdmin),

        'nomeGestAmb': json.dumps(nomeGestAmb),
        'valorGestAmb': json.dumps(valorGestAmb),

        'nomeSeguranca': json.dumps(nomeSeguranca),
        'valorSeguranca': json.dumps(valorSeguranca),

        'nomeCultura': json.dumps(nomeCultura),
        'valorCultura': json.dumps(valorCultura),

        'nomeAssSocial': json.dumps(nomeAssSocial),
        'valorAssSocial': json.dumps(valorAssSocial),

        'nomeSaneamento': json.dumps(nomeSaneamento),
        'valorSaneamento': json.dumps(valorSaneamento),

        'nomeAgricultura': json.dumps(nomeAgricultura),
        'valorAgricultura': json.dumps(valorAgricultura),

        'nomeTransportes': json.dumps(nomeTransportes),
        'valorTransportes': json.dumps(valorTransportes),

        'nomeUrbanismo': json.dumps(nomeUrbanismo),
        'valorUrbanismo': json.dumps(valorUrbanismo),

        'nomeEncEspeciais': json.dumps(nomeEncEspeciais),
        'valorEncEspeciais': json.dumps(valorEncEspeciais),

        'nomeDirCidadania': json.dumps(nomeDirCidadania),
        'valorDirCidadania': json.dumps(valorDirCidadania),

        'nomeSaudePopul': json.dumps(nomeSaudePopul),
        'valorSaudePopul': json.dumps(valorSaudePopul),
        'nomeEducacaoPopul': json.dumps(nomeEducacaoPopul),
        'valorEducacaoPopul': json.dumps(valorEducacaoPopul),
        'nomeAdminPopul': json.dumps(nomeAdminPopul),
        'valorAdminPopul': json.dumps(valorAdminPopul),
        
        'cidade2': cidade2,
        'mediaSaudeLista_labels': json.dumps(mediaSaudeLista_labels),
        'mediaSaudeLista_valor': json.dumps(mediaSaudeLista_valor),
        # 'nomeDirCidadania': json.dumps(nomeDirCidadania),
        # 'valorDirCidadania': json.dumps(valorDirCidadania),
    }

    template_name = 'tInform/index.html'
    cont = 0
    return render(request, template_name, contexto)


def relatorio(request, slug):
    global data_Final
    global data_Inicial

    cidades = Cidade.objects.get(slug=slug)
    contexto = {}
    # ===============================
    # VARIAVEIS USADAS NO FORMULARIOS
    is_valid = False

    listaOrgao = None
    listaElemento = None
    listaSubFuncao = None
    listaFuncao = None
    listaProjeto = None
    listaDiarias = None

    if request.method != 'POST':
        print("relatorio NPOST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        dados = SearchClasses()

        listaOrgao = dados.buscaDadosOrgao(
            con, cidades.idCliente, data_Inicial, data_Final)
        listaElemento = dados.buscaDadosElemento(
            con, cidades.idCliente, data_Inicial, data_Final)
        listaFuncao = dados.buscaDadosFuncao(
            con, cidades.idCliente, data_Inicial, data_Final)
        listaSubFuncao = dados.buscaDadosSubFuncao(
            con, cidades.idCliente, data_Inicial, data_Final)
        listaProjeto = dados.buscaDadosProjeto(
            con, cidades.idCliente, data_Inicial, data_Final)
        listaDiarias = dados.buscaDadosDiarias(
            con, cidades.idCliente, data_Inicial, data_Final)

    if request.method == 'POST':
        print("relatorio POST")
        print("data_Inicial:", data_Inicial)
        print("data_Final:", data_Final)
        form = SearchForm(request.POST)
        if form.is_valid():
            is_valid = True
            data_Final = form.cleaned_data['dataFinal']
            data_Inicial = form.cleaned_data['dataInicial']
            listaOrgao = form.buscaDadosOrgao(con, cidades.idCliente)
            print(listaOrgao)
            listaElemento = form.buscaDadosElemento(con, cidades.idCliente)
            listaFuncao = form.buscaDadosFuncao(con, cidades.idCliente)
            listaSubFuncao = form.buscaDadosSubFuncao(
                con, cidades.idCliente)
            listaProjeto = form.buscaDadosProjeto(con, cidades.idCliente)
            listaDiarias = form.buscaDadosDiarias(con, cidades.idCliente)
            # limpa formulario
            # form = SearchForm(None)
    else:
        form = SearchForm()

    # ======================================================================
    # convertendo flot para moeda brasileira
    for xx in listaOrgao:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        xx["soma"] = locale.currency(xx["soma"], grouping=True, symbol=None)

    for xx in listaElemento:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        xx["soma"] = locale.currency(xx["soma"], grouping=True, symbol=None)

    for xx in listaSubFuncao:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        xx["soma"] = locale.currency(xx["soma"], grouping=True, symbol=None)

    for xx in listaFuncao:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        xx["soma"] = locale.currency(xx["soma"], grouping=True, symbol=None)

    for xx in listaProjeto:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        xx["soma"] = locale.currency(xx["soma"], grouping=True, symbol=None)

    for xx in listaDiarias:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        xx["soma"] = locale.currency(xx["soma"], grouping=True, symbol=None)
    lista = sorted(listaOrgao, key=lambda k: k['soma'])

    # =======================================================================
    # contexto com as variaveis para os templates
    contexto = {
        'cidade': cidades,
        'id': cidades.idCliente,
        # lista de dados para relatorio
        'listaOrgao':  listaOrgao,
        'listaElemento': listaElemento,
        'listaFuncao': listaFuncao,
        'listaSubFuncao': listaSubFuncao,
        'listaProjeto': listaProjeto,
        'listaDiarias': listaDiarias,
        'listaFuncao2': json.dumps(listaFuncao),
        # fimlistas
        'form': form,
        'is_valid': is_valid,
        'dataInicial': data_Inicial,
        'dataFinal': data_Final,
    }
    # ========================================================================

    template_name = 'tInform/tables.html'
    return render(request, template_name, contexto)


def details(request, slug):

    global data_Inicial
    global data_Final

    data_Final = None
    data_Inicial = None
    
    cidades = Cidade.objects.get(slug=slug)
    contexto = {}

    contexto = {
        'cidade': cidades,

    }

    template_name = 'tcidades/details2.html'
    return render(request, template_name, contexto)


# ================================================================= FIM ARQUIVO ================================================================

            # nomeIDclientePopul=None

            # with con.cursor() as cursor:
            #     cursor.execute(
            #         "SELECT NOME_MUNICIPIO, POPULACAO FROM Prefeitura2.Populacao")  # noqa E501
            # municipiosLista = cursor.fetchall()
            # print("===================================")
            # for m in municipiosLista:
            #     if str(m['NOME_MUNICIPIO']) in str(cidades):
            #         print(m['NOME_MUNICIPIO'])
            #         quantPopul = m['POPULACAO']
            #         print(quantPopul)
            # print("===================================")
            # print(cidades)
            # print(municipiosLista[0]["NOME_MUNICIPIO"])
                       # print("============================================================================")
            # for x in listaDicFuncoes:
            #     indice = 0
            #     while indice < len(x):
            #         print("============================")
            #         if str(x[indice]["divisao"]) > "00":
            #             print(x[indice]["divisao"])
            #             print(x[indice]["soma"])
            #             if x[indice]["divisao"] not in listaQuantFuncoes:
            #                 listaQuantFuncoes = {"funcao": x[indice]["divisao"], "total": 0.0} 
            #             indice = indice + 1
            #         else:
            #             indice = indice + 1
            # print("============================================================================")
            # listaQuantFuncoes={}
            # listaQuantFuncoes2=[]
            # print("============================================================================")
            # for x in listaDicFuncoes:
            #     indice = 0
            #     while indice < len(x):
            #         print("============================")
            #         if str(x["listaDeFuncoes"][indice]["divisao"]) != " - ":
            #             print(x["listaDeFuncoes"][indice]["divisao"])
            #             print(x["listaDeFuncoes"][indice]["soma"])

            #             indice = indice + 1
            #         else:
            #             indice = indice + 1
            # print("============================================================================")
            # print(listaQuantFuncoes)
            # for funcao in listaQuantFuncoes:
            #     print(funcao["funcao"] +":"+ funcao["total"])

            # conversoes para JASON


            # # ===================================================== ALgoritmo de media ===========================================================
            # listaDicFuncoes = form.retornaFuncaoPorPopul(con)
            # nomeIDclientePopul = listaDasCidades(con)

            # for x in listaDicFuncoes:
            #     indice=0
            #     # print(x["idCliente"]["idCliente"])
            #     # print("-----------------------------------------------------------------------------------------------------------------------")
            #     while indice < len(x["listaFuncoes"]):
            #         if (x["listaFuncoes"][indice]["divisao"]).upper() == "10 - SAUDE":
            #             idClienteValorSaude.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})
            #         # print(x["listaFuncoes"][indice]["divisao"])
            #         # print(x["listaFuncoes"][indice]["soma"])

            #         if (x["listaFuncoes"][indice]["divisao"]).upper() == "04 - ADMINISTRACAO":
            #             idClienteValorAdm.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

            #         if (x["listaFuncoes"][indice]["divisao"]).upper() == "12 - EDUCACAO":
            #             idClienteValorEducacao.append({"idCliente": x["idCliente"]["idCliente"], "valor": float(x["listaFuncoes"][indice]["soma"])})

            #         indice += + 1



        

            # print("LISTA SAUDE")
            # for x in idClienteValorSaude:
            #     print(x)
            # print("LISTA EDUCAÇÃO")
            # for x in idClienteValorEducacao:
            #     print(x)            
            # print("LISTA ADMINISTRACAO")
            # for x in idClienteValorAdm:
            #     print(x)
            # # for x in listaCidades:
            # #     print(x)

            # print("Lista das cidades")
            # for x in nomeIDclientePopul:
            #     print(x)

            # idNomePopul_lista = []
            # print("LISTA MEDIA SAUDE")
            # for n in idClienteValorSaude:
            #     for m in nomeIDclientePopul:
            #         if n["idCliente"] == m["idCliente"]: 
            #             # print("COMPARANDO")
            #             # print(n["idCliente"] == m["idCliente"])
            #             idNomePopul_lista.append( { "idCliente": n["idCliente"], "nome": m["nome"], "media": round( ( float(n["valor"] ) / int( m["populacao"].replace(".", "")) ), 2) } )   
            #             print(m["populacao"])
            #             print(n["valor"])

            # # for x in idNomePopul_lista:
            # #     print(x)
            # mediaSaudeLista_labels = [obj['nome'][24:] for obj in idNomePopul_lista]
            # mediaSaudeLista_valor = [obj['media'] for obj in idNomePopul_lista]
            # # =========================================================== FIm ====================================================================