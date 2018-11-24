import pymysql.cursors
from siteTransp.apiWebDados import Empenho
from siteTransp.apiWebDados import Cliente
from siteTransp.apiWebDados import Gerenciador
import time

dataInicio = "31/07/2017"
dataFim = "31/08/2017"
empenho = Empenho.Empenho()



# Gerenciador.limpaDadosBanco("Empenho")
# Gerenciador.limpaDadosBanco("Pagamento")
#Gerenciador.limpaDadosBanco("Cliente")
# Gerenciador.limpaDadosBanco("Favorecido")
#Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")
ini = time.time()
Gerenciador.recuperaEmpenhoInsereBanco(245,dataInicio,dataFim)
Gerenciador.recuperaPagamentoInsereBanco(245,dataInicio,dataFim)
fim = time.time()
print ("TEMPO DE EXECUCAO "+str( fim-ini))
