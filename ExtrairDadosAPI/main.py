import pymysql.cursors
import Empenho
import Cliente
import Gerenciador

empenho = Empenho.Empenho()

#adm = Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")
Gerenciador.recuperaEmpenhoInsereBanco(245)


