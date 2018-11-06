import pymysql.cursors
import Empenho
import Cliente
import Gerenciador
import time
import json

stringTeste = "Prefeitura Municipal de Ilhéus"

# print(stringTeste.split("Prefeitura Municipal de ")[1].lower())


# string1 = 'HeLlO'
# string2 = 'ilhéus'
# try:
#     if stringTeste.split("Prefeitura Municipal de ")[1].lower() == string2.lower():
#         print ("aaaa")
#     else:
#         print ("bbb")
# except:
#     print("Não é municipio")


Gerenciador.recuperaIdIBGECidades()
# Gerenciador.recuperaDadosIGBE()

# Gerenciador.recuperaMortalidadeInfantil()
# Gerenciador.recuperaPopulacao()
# Gerenciador.limpaDadosBanco("HistoricoMetrica")
# Gerenciador.limpaDadosBanco("Empenho")
# Gerenciador.limpaDadosBanco("Pagamento")
# Gerenciador.limpaDadosBanco("Cliente")
# Gerenciador.limpaDadosBanco("Favorecido")
# ini = time.time()
# # Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")
#
#
#
# dataInicio = "01/01/2017"
# dataFim = "31/12/2017"
# empenho = Empenho.Empenho()
#
# listaClientes = Gerenciador.retornaCidadesComEmpenho()
#
#
# for cliente in listaClientes:
#
#     Gerenciador.recuperaEmpenhoInsereBanco(cliente.idcliente,dataInicio,dataFim)
#     Gerenciador.recuperaPagamentoInsereBanco(cliente.idcliente,dataInicio,dataFim)
#     fim = time.time()
#     print ("TEMPO DE EXECUCAO "+str( fim-ini))
#     break
