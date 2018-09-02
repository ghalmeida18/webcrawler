from django.shortcuts import render
# from django.http import HttpResponse
# from django.db.models import Sum
# from simplemooc.core.models import Empenho
import simplejson
# from six.moves import configparser
# from django.http import JsonResponse
from django.shortcuts import render_to_response
# from decimal import Decimal
# import simplejson as json
import pymysql.cursors


# apagar: Como eu achei pouco intuitivo o metodo do DJANGO tratar o banco, eu utilizei uma conexão mais "manual", com SQL direto. Sinta-se a vontade para trocar. :)


con = pymysql.connect(host='127.0.0.1',
                      user='root',  # insira aqui o seu usuario, é root?
                      passwd='jose123',  # insira aqui a senha so seu banco
                      db='Prefeitura',
                      cursorclass=pymysql.cursors.DictCursor
                      )


# def home(request):
#	with con.cursor() as cursor:
#
#			cursor.execute("SELECT Orgao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Orgao Order By soma")
#			dados = cursor.fetchall()
#
#			return render_to_response('inicio.html',{'orgaos':simplejson.dumps(dados)})

def home(request):
    with con.cursor() as cursor:

        cursor.execute(
            "SELECT Orgao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Orgao Order By soma")
        orgao = cursor.fetchall()

        cursor.execute(
            "SELECT Elemento AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Elemento Order By soma")
        elemento = cursor.fetchall()

        cursor.execute(
            "SELECT Funcao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Funcao Order By soma")
        funcao = cursor.fetchall()

        cursor.execute(
            "SELECT SubFuncao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By SubFuncao Order By soma")
        subfuncao = cursor.fetchall()

        cursor.execute(
            "SELECT Projeto AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Projeto Order By soma")
        projeto = cursor.fetchall()

        cursor.execute(
            "SELECT Destinacao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Destinacao Order By soma")
        destinacao = cursor.fetchall()

        cursor.execute(
            "SELECT MONTH(DataPagamento) as divisao, Sum(ValorPagamento) as soma From Pagamento GROUP BY MONTH(DataPagamento);")
        pormes = cursor.fetchall()

        cursor.execute("SELECT Nome, Sum(ValorPagamento) soma From Favorecido NATURAL JOIN Empenho Natural Join Pagamento WHERE Elemento = '3.3.90.14.05 - Diarias De Demais Servidores' GROUP BY Nome ORDER BY soma;")
        Ddiarias = cursor.fetchall()

        cursor.execute(
            "SELECT Elemento, SUM(ValorPagamento) soma From Empenho NATURAL JOIN Pagamento WHere Elemento = '3.1.90.11.07 - Subsidio Do Prefeito';")
        SubsPrefeito = cursor.fetchall()

        cursor.execute("SELECT Nome nome, COUNT(*) qtd FROM Favorecido Natural join Empenho Natural Join Pagamento Where Elemento = '3.3.90.14.05 - Diarias De Demais Servidores' GROUP BY nome ORDER BY qtd ;")
        qtdDiarias = cursor.fetchall()

        cursor.execute(
            "SELECT Nome, Cargo  FROM Favorecido NATURAL JOIN Empenho WHERE Elemento = '3.3.90.14.05 - Diarias De Demais Servidores' GROUP BY Nome;")
        CargosD = cursor.fetchall()

        cursor.execute("SELECT Nome divisao, SUM(ValorPagamento) soma FROM Favorecido Natural JOIN Empenho NATURAL JOIN Pagamento WHERE Elemento = '3.3.90.39.22 - Multas Indedutiveis' GROUP BY Nome ORDER BY soma;")
        Multas = cursor.fetchall()

        return render_to_response('inicio.html', {'orgao': simplejson.dumps(orgao),
                                                  'elemento': simplejson.dumps(elemento),
                                                  'funcao': simplejson.dumps(funcao),
                                                  'subfuncao': simplejson.dumps(subfuncao),
                                                  'projeto': simplejson.dumps(projeto),
                                                  'destinacao': simplejson.dumps(destinacao),
                                                  'pormes': simplejson.dumps(pormes),
                                                  'Ddiarias': simplejson.dumps(Ddiarias),
                                                  'SubsPrefeito': simplejson.dumps(SubsPrefeito),
                                                  'qtdDiarias': simplejson.dumps(qtdDiarias),
                                                  'Cargos': simplejson.dumps(CargosD),
                                                  'Multas': simplejson.dumps(Multas)

                                                  })


def contact(request):
    return render(request, 'contact.html')  # tela de contato


def graficos(request):

    with con.cursor() as cursor:

        cursor.execute(
            "SELECT Orgao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Orgao Order By soma")
        dados = cursor.fetchall()

        return render_to_response('graficos.html', {'orgaos': simplejson.dumps(dados)})


def g(request):

    with con.cursor() as cursor:

        cursor.execute(
            "SELECT Elemento AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Elemento Order By soma")
        dados = cursor.fetchall()

        return render_to_response('graficos.html', {'orgaos': simplejson.dumps(dados)})


def porano(request):

    with con.cursor() as cursor:

        cursor.execute(
            "SELECT MONTH(DataPagamento) as divisao, Sum(ValorPagamento) as soma From Pagamento GROUP BY MONTH(DataPagamento);")
        dados = cursor.fetchall()

        return render_to_response('graficos.html', {'orgaos': simplejson.dumps(dados)})


def dashboard(request):

    with con.cursor() as cursor:

        cursor.execute(
            "SELECT Orgao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento Group By Orgao Order By soma")
        dados = cursor.fetchall()

        return render_to_response('dashboard.html', {'orgaos': simplejson.dumps(dados)})

    #orgaos = list(Empenho.objects.values('Orgao').annotate(Sum('Valor')))


# Empenho.objects.values('Orgao').annotate(Sum('Valor'))
