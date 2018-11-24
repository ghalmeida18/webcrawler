from django import forms
from operator import itemgetter

# from siteTransp.apiWebDados import Gerenciador
# from .models import Cidade


class SearchForm(forms.Form):
    # TODO: Define form fields here
    dataInicial = forms.CharField(label='Data inicial', required=True)
    dataFinal = forms.CharField(label='Data final', required=True)

    def buscaDadosOrgao(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT Orgao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' Group By Orgao")  # noqa E501
            listaSomaOrgao = cursor.fetchall()

        return listaSomaOrgao

    def buscaDadosElemento(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT Elemento AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento  where idCliente =" + str(idCliente) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' Group By Elemento")
            listaSomaElemento = cursor.fetchall()

        return listaSomaElemento

    def buscaDadosFuncao(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT Funcao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' Group By Funcao")
            listaSomaFuncao = cursor.fetchall()

        return listaSomaFuncao

    def buscaDadosSubFuncao(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT SubFuncao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' Group By SubFuncao ")
            listaSomaSubFuncao = cursor.fetchall()

        return listaSomaSubFuncao

    def buscaDadosProjeto(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT Projeto AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' Group By Projeto order by  soma desc")
            listaProjeto = cursor.fetchall()

        return listaProjeto

    def buscaDadosDestinacao(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute(
                "SELECT Destinacao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP By divisao ")
            listaDestinacao = cursor.fetchall()

        return listaDestinacao

    def buscaDadosDiarias(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute("SELECT Nome, Sum(ValorPagamento) soma From Favorecido NATURAL JOIN Empenho Natural Join Pagamento WHERE idCliente =" + str(
                idCliente) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "'GROUP BY Nome order by soma desc;")
            listaDiarias = cursor.fetchall()

        return listaDiarias

    # FUNCAO QUE RETORNA LISTA DE FUNOCES POR PREFEITURA
    def retornaListaFuncoes(self, con, idCliente):
        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT Funcao AS divisao FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " Group By Funcao")
            listaFuncoes = cursor.fetchall()

        return listaFuncoes

    def retornaDicFuncoes(self, con, idCliente, listaFuncoes):
        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        listaDicFuncoes = []
        with con.cursor() as cursor:
            for funcao in listaFuncoes:
                cursor.execute(
                    "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao= '" + str(funcao) + "' AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
                listaDicFuncoes.append(cursor.fetchall())

        return listaDicFuncoes

    def retornaFuncaoPorPopul(self, con):
        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        lista = []
        with con.cursor() as cursor:

            cursor.execute(
                "SELECT  idCliente FROM Prefeitura.Cliente ;")
            idClienteLista = cursor.fetchall()

            for idc in idClienteLista:

                cursor.execute(
                    "SELECT Funcao AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idc['idCliente']) + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' Group By Funcao")
                lista.append(
                    {"idCliente": idc, "listaFuncoes": cursor.fetchall()})
                # lista.append(cursor.fetchall())
        return lista

    # ===============================================================================================================================
    # FUNCOES QUE RETORNAM VALORES ORDENADOS POR DATA
    def buscaSaudePorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        # print(dataInicial)
        # print(dataFinal)

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente ='" + str(idCliente) + "' AND Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaEducacaoPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND Funcao='12 - EDUCACAO'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaAdministracaoPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='04 - ADMINISTRACAO'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaGestaoAmbPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='18 - GESTAO AMBIENTAL'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaAgriculturaPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='18 - GESTAO AMBIENTAL'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaSegurancaPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='06 - SEGURANCA PUBLICA'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaAssSocialPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='08 - ASSISTENCIA SOCIAL'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaSaneamentoPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaTransportesPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaEncEspeciaisPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaCulturaPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaUrbanismoPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    def buscaDirCidadaniaPorData(self, con, idCliente):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:

            cursor.execute(
                "SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente =" + str(idCliente) + " AND  Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)

        return FuncaoPorData

    # ===============================================================================================================================
    # retorna informacoes dividada pela populacao
    def buscaSaudePorPopul(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        print(dataInicial)
        print(dataFinal)

        with con.cursor() as cursor:
            cursor.execute("SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente ='" + str(idCliente) +
                           "' AND Funcao='10 - SAUDE'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)
        # print(int(populTotal(con, cidade).replace(".", "")))

        i = 0
        while i < len(FuncaoPorData):
            div = populTotal(con, cidade)
            FuncaoPorData[i]["soma"] = float(
                FuncaoPorData[i]["soma"]) / int(populTotal(con, cidade).replace(".", ""))
            i = i + 1
        # print(FuncaoPorData)

        return FuncaoPorData

    def buscaEducacaoPopul(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute("SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente ='" + str(idCliente) +
                           "' AND Funcao='12 - EDUCACAO'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)
        # print(int(populTotal(con, cidade).replace(".", "")))

        i = 0
        while i < len(FuncaoPorData):
            div = populTotal(con, cidade)
            FuncaoPorData[i]["soma"] = float(
                FuncaoPorData[i]["soma"]) / int(populTotal(con, cidade).replace(".", ""))
            i = i + 1
        # print(FuncaoPorData)

        return FuncaoPorData

    def buscaAdministracaoPopul(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute("SELECT MONTH(DataPagamento) AS divisao, SUM(ValorPagamento) soma FROM Empenho NATURAL JOIN Pagamento where idCliente ='" + str(idCliente) +
                           "' AND Funcao='04 - ADMINISTRACAO'" + " AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY MONTH(DataPagamento)")
            FuncaoPorData = cursor.fetchall()

        FuncaoPorData = alteraMes(FuncaoPorData)
        # print(int(populTotal(con, cidade).replace(".", "")))

        i = 0
        while i < len(FuncaoPorData):
            div = populTotal(con, cidade)
            FuncaoPorData[i]["soma"] = float(
                FuncaoPorData[i]["soma"]) / int(populTotal(con, cidade).replace(".", ""))
            i = i + 1
        # print(FuncaoPorData)

        return FuncaoPorData


    def buscaDiaAdm(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute( "SELECT YEAR(DataPagamento) as ano, WEEK(DataPagamento) as semana, SUM(ValorPagamento) as soma FROM Empenho NATURAL JOIN Pagamento where idCliente='" + str(idCliente) + "' AND  Funcao='04 - ADMINISTRACAO' AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY ano, semana;")
            FuncaoPorData = cursor.fetchall()

        return FuncaoPorData

    def buscaDiaSaude(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute( "SELECT YEAR(DataPagamento) as ano, WEEK(DataPagamento) as semana, SUM(ValorPagamento) as soma FROM Empenho NATURAL JOIN Pagamento where idCliente='" + str(idCliente) + "' AND  Funcao='10 - SAUDE' AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY ano, semana;")
            FuncaoPorData = cursor.fetchall()

        return FuncaoPorData

    def buscaDiaSeguranca(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute( "SELECT YEAR(DataPagamento) as ano, WEEK(DataPagamento) as semana, SUM(ValorPagamento) as soma FROM Empenho NATURAL JOIN Pagamento where idCliente='" + str(idCliente) + "' AND  Funcao='06 - SEGURANCA PUBLICA' AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY ano, semana;")
            FuncaoPorData = cursor.fetchall()

        return FuncaoPorData

    def buscaDiaSaneamento(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute( "SELECT YEAR(DataPagamento) as ano, WEEK(DataPagamento) as semana, SUM(ValorPagamento) as soma FROM Empenho NATURAL JOIN Pagamento where idCliente='" + str(idCliente) + "' AND  Funcao='17 - SANEAMENTO' AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY ano, semana;")
            FuncaoPorData = cursor.fetchall()

        return FuncaoPorData

    def buscaDiaSocial(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute( "SELECT YEAR(DataPagamento) as ano, WEEK(DataPagamento) as semana, SUM(ValorPagamento) as soma FROM Empenho NATURAL JOIN Pagamento where idCliente='" + str(idCliente) + "' AND  Funcao='08 - ASSISTENCIA SOCIAL' AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY ano, semana;")
            FuncaoPorData = cursor.fetchall()

        return FuncaoPorData


    def buscaDiaEducacao(self, con, idCliente, cidade):

        dataFinal = self.cleaned_data['dataFinal']
        dataInicial = self.cleaned_data['dataInicial']

        dataInicial = str(dataInicial[6:10] + "-" +
                          dataInicial[3:5] + "-" + dataInicial[0:2])
        dataFinal = str(dataFinal[6:10] + "-" +
                        dataFinal[3:5] + "-" + dataFinal[0:2])

        with con.cursor() as cursor:
            cursor.execute( "SELECT YEAR(DataPagamento) as ano, WEEK(DataPagamento) as semana, SUM(ValorPagamento) as soma FROM Empenho NATURAL JOIN Pagamento where idCliente='" + str(idCliente) + "' AND  Funcao='12 - EDUCACAO' AND DataPagamento >= '" + str(dataInicial) + "' AND DataPagamento <= '" + str(dataFinal) + "' GROUP BY ano, semana;")
            FuncaoPorData = cursor.fetchall()

        return FuncaoPorData       
# SELECT year(DataPagamento) as ano , MONTH(DataPagamento) AS mes, day(DataPagamento) as dia , SUM(ValorPagamento) soma 
# FROM Empenho NATURAL JOIN Pagamento 
# where idCliente =245=
# GROUP BY ano, mes, dia 
# order by ano, mes, dia;


def alteraMes(meses):

    for mes in meses:

        if mes["divisao"] == 1:
            mes["divisao"] = "Jan"
        if mes["divisao"] == 2:
            mes["divisao"] = "Fev"
        if mes["divisao"] == 3:
            mes["divisao"] = "Mar"
        if mes["divisao"] == 4:
            mes["divisao"] = "Abr"
        if mes["divisao"] == 5:
            mes["divisao"] = "Mai"
        if mes["divisao"] == 6:
            mes["divisao"] = "Jun"
        if mes["divisao"] == 7:
            mes["divisao"] = "Jul"
        if mes["divisao"] == 8:
            mes["divisao"] = "Ago"
        if mes["divisao"] == 9:
            mes["divisao"] = "Set"
        if mes["divisao"] == 10:
            mes["divisao"] = "Out"
        if mes["divisao"] == 11:
            mes["divisao"] = "Nov"
        if mes["divisao"] == 12:
            mes["divisao"] = "Dez"

    return meses


def populTotal(con, cidade):

    with con.cursor() as cursor:
        cursor.execute(
            "SELECT NOME_MUNICIPIO, POPULACAO FROM Prefeitura.Populacao")  # noqa E501
    municipiosLista = cursor.fetchall()
    for m in municipiosLista:
        if str(m['NOME_MUNICIPIO']) in str(cidade):
            # print(m['NOME_MUNICIPIO'])
            quantPopul = m['POPULACAO']
            # print(quantPopul)

    return quantPopul


def listaDasCidades(con):
    lista_NomeIDclientePopulacao = []

    with con.cursor() as cursor:
        cursor.execute(
            "SELECT NOME_MUNICIPIO, POPULACAO FROM Prefeitura.Populacao")  # noqa E501
    nomePopul = cursor.fetchall()

    with con.cursor() as cursor:
        cursor.execute("SELECT  idCliente, nome FROM Prefeitura.Cliente;")  # noqa E501
    idClienteNome = cursor.fetchall()

    for m in idClienteNome:
        for n in nomePopul:
            if ("Prefeitura Municipal de "+n["NOME_MUNICIPIO"]) == m["nome"]:
                lista_NomeIDclientePopulacao.append({"idCliente": m["idCliente"],"nome": m["nome"] , "populacao": n['POPULACAO'] })

    return lista_NomeIDclientePopulacao


# AGRUPAMENTO POR DIA
# SELECT YEAR(DataPagamento) AS ano, DATE_FORMAT(DataPagamento, '%b %e') AS semana, SUM(ValorPagamento) soma 
# FROM Empenho NATURAL JOIN Pagamento where idCliente ="245" AND  Funcao='04 - ADMINISTRACAO' AND DataPagamento >= '2017-01-01' AND DataPagamento <= '2017-12-31' 
# GROUP BY ano, semana;

# SELECT year(DataPagamento) as ano , MONTH(DataPagamento) AS mes, day(DataPagamento) as dia , SUM(ValorPagamento) soma 
# FROM Empenho NATURAL JOIN Pagamento 
# where idCliente =245 
# GROUP BY ano, mes, dia 
# order by ano, mes, dia;

# CODIGO PARA ORDENAR LISTA DE DICIONARIOOS
# funcao = sorted(FuncaoPorData, key=lambda k: k['soma']) 
# for y in funcao:
#     print(y)

# AGRUPAR POR SEMANA
# SELECT YEAR(DataPagamento) as ano, WEEK(DataPagamento) as semana, SUM(ValorPagamento) as soma 
# FROM Empenho NATURAL JOIN Pagamento 
# where idCliente ='245' 
# AND  Funcao='04 - ADMINISTRACAO' 
# #AND DataPagamento >= '2017-02-01' AND DataPagamento <= '2017-03-02'
# GROUP BY ano, semana;