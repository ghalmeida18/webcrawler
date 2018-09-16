import pymysql.cursors
import Empenho
import Cliente
import Gerenciador
import time



# Gerenciador.limpaDadosBanco("Empenho")
# Gerenciador.limpaDadosBanco("Pagamento")
# Gerenciador.limpaDadosBanco("Cliente")
# Gerenciador.limpaDadosBanco("Favorecido")
ini = time.time()
# Gerenciador.recuperaClientesInsereBanco("http://transparencia.portalfacil.com.br/api/clientes?type=json")



dataInicio = "01/01/2017"
dataFim = "31/12/2017"
empenho = Empenho.Empenho()


listaClientes = Gerenciador.retornaCidadesComEmpenho()
print(len(listaClientes))
for cliente in listaClientes:
    if(cliente.idcliente==279):
        # Gerenciador.recuperaEmpenhoInsereBanco(cliente.idcliente,dataInicio,dataFim)
        Gerenciador.recuperaPagamentoInsereBanco(cliente.idcliente,dataInicio,dataFim)
        fim = time.time()
        print ("TEMPO DE EXECUCAO "+str( fim-ini))
        break
