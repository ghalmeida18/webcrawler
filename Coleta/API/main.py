import pymysql.cursors
import Empenho
import Cliente
import Gerenciador

empenho = Empenho.Empenho()

<<<<<<< HEAD
Gerenciador.limpaDadosBanco("Empenho")
Gerenciador.limpaDadosBanco("Pagamento")
Gerenciador.limpaDadosBanco("Cliente")
Gerenciador.limpaDadosBanco("Favorecido")

Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")
Gerenciador.recuperaEmpenhoInsereBanco(7,dataInicio,dataFim)
Gerenciador.recuperaPagamentoInsereBanco(7,dataInicio,dataFim)
=======
Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")
Gerenciador.recuperaEmpenhoInsereBanco(245)
Gerenciador.recuperaPagamentoInsereBanco(245)
>>>>>>> parent of 11e3b63... Adicionado dataInicio dataFim nos parametros
