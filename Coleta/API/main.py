import pymysql.cursors
import Empenho
import Cliente
import Gerenciador

dataInicio = "01/01/2017"
dataFim = "31/12/2017"
empenho = Empenho.Empenho()

Gerenciador.limpaDadosBanco("Empenho")
Gerenciador.limpaDadosBanco("Pagamento")
#Gerenciador.limpaDadosBanco("Cliente")
Gerenciador.limpaDadosBanco("Favorecido")
#Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")
Gerenciador.recuperaEmpenhoInsereBanco(245,dataInicio,dataFim)
#Gerenciador.recuperaPagamentoInsereBanco(245,dataInicio,dataFim)
