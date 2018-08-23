import pymysql.cursors
import Empenho
import Cliente
import Gerenciador

empenho = Empenho.Empenho()

Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")
Gerenciador.recuperaEmpenhoInsereBanco(245)
Gerenciador.recuperaPagamentoInsereBanco(245)
