import json
import requests
import pymysql.cursors
from datetime import datetime
import sys
import time

from siteTransp.apiWebDados import Pagamento
from siteTransp.apiWebDados import Cliente
from siteTransp.apiWebDados import Empenho



def conectaBanco():
	con = pymysql.connect(host = '127.0.0.1',
                      	      user = 'root',
                              passwd='jose123',
                              db = 'Prefeitura',
                              cursorclass=pymysql.cursors.DictCursor)
	return con

def recuperaClientesInsereBanco(link):

	con = conectaBanco()

	cidades = []

	r = requests.get(link)
	if r.status_code == 200:
		reddit_data = json.loads(r.content)
		for reddit in reddit_data:
			try:
				cidades.append(Cliente.Cliente(reddit['IdCliente'],reddit['DescCliente']))
				sql = "INSERT INTO Cliente(nome,idcliente) values ('"+reddit['DescCliente']+"',"+reddit['IdCliente']+")"
				cursor = con.cursor()
				cursor.execute(sql)
				con.commit()
				#print(reddit['DescCliente']+" "+reddit['IdCliente'])

			except :
				print("Erro ao inserir cidade")
	con.close()

def recuperaEmpenhoInsereBanco(idCliente,dataInicio,dataFim):



	controlador = True

	contadorEmpenhos = 0
	pagina = 1

	while controlador:



		link = "http://transparencia.portalfacil.com.br/api/empenhos?type=json&idCliente="+str(idCliente)+"&page="+str(pagina)+"&pageSize=100&dtInicio="+dataInicio+"&dtFim="+dataFim
		print(link)
		con = conectaBanco()
		listaEmpenhos = []

		try:
			r = requests.get(link)
			if r.status_code == 200:
				reddit_data = json.loads(r.content)
				if len(reddit_data)==21:
					print("FIM DE RECUPERACAO DE EMPENHOS")
					return
				for reddit in reddit_data:
					try:

						empenho = Empenho.Empenho()

						empenho.numero=reddit['NumEmpenho']
						empenho.especie = reddit['TpEmpenho']
						empenho.orgao = reddit['NumUnidade']+" "+ reddit['DescUnidade']
						empenho.projeto = "=========PROJETOTESTE========"
						empenho.elemento =  reddit['NumDespesa']+" "+ reddit['DescDespesa']
						empenho.licitacao = reddit['NumLicitacao']+" - "+reddit['DtLicitacao']+" - "+reddit['TpLicitacao']

						empenho.processo = reddit['NumProcesso']
						empenho.dataEmpenho = reddit['DtEmpenho']

						data  = datetime.strptime(empenho.dataEmpenho,"%d/%m/%Y").strftime("%Y-%m-%d")

						empenho.valor = reddit['VlEmpenho']
						empenho.empenho_Numero = reddit['NumEmpenho']

						empenho.funcao = reddit['NumFuncao']+" - "+reddit['DescFuncao']
						empenho.subFuncao = reddit['NumSubFuncao']+" - "+reddit['DescSubFuncao']
						empenho.programa = reddit['NumPrograma']+" - "+reddit['DescPrograma']
						empenho.destinacao = reddit['NumDestinacao']+" - "+reddit['DescDestinacao']

						#INSERINDO FAVORECIDO
						empenho.insereFavorecido(reddit['DescFornecedor'],reddit['NumCpfCnpjFornecedor'],"=====CARGO TESTE=====")

						cursor = con.cursor()
						#INSERE NOVO FAVORECIDO CASO NÃO TENHA NO BANCO DE DADOS
						if(not(cursor.execute("SELECT * from Favorecido where Nome = '" + empenho.retornaFavorecido().retornaNome() + "'"))):
							sqlquery = "INSERT INTO Favorecido(CPF_CNPJ, Nome, Cargo,idCliente) VALUES (%s, %s, %s, %s);"
							cursor.execute(sqlquery,(
							        empenho.retornaFavorecido().CPF_CNPJ,
							        empenho.retornaFavorecido().retornaNome(),
							        empenho.retornaFavorecido().retornaCargo(),
									str(idCliente)
							        ))
							con.commit()

						#RETORNA O ID DO FAVORECIDO ADICIONADO
						cursor.execute("SELECT IdFavorecido from Favorecido where Nome = '"+empenho.retornaFavorecido().retornaNome()+"'")
						IdRetornado = cursor.fetchone()
						idFavorecido = str(IdRetornado['IdFavorecido'])
						#INSERE EMPENHO
						sqlquery = "INSERT INTO Empenho(Especie,Orgao,Projeto,Elemento,Licitacao,Processo,DataEmpenho,Valor,NumeroEmpenho,IdFavorecido,Funcao,SubFuncao,Programa,Destinacao,idCliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

						cursor.execute(sqlquery,(
							empenho.especie,
							empenho.orgao,
							empenho.projeto,
							empenho.elemento,
							empenho.licitacao,
							empenho.processo,
							data,
							empenho.valor,
							empenho.numero,
							idFavorecido,
							empenho.funcao,
							empenho.subFuncao,
							empenho.programa,
							empenho.destinacao,
							str(idCliente)
							))
						con.commit()

						contadorEmpenhos = contadorEmpenhos + 1
						print("Empenho {}".format (contadorEmpenhos))
						sys.stdout.write("\033[F")
						time.sleep(0.1)

					except:
						print("Erro empenho")
			pagina = pagina +1
		except:
			print("ERRO DE CONEXÃO EMPENHO")
			#return


	con.close()


def recuperaPagamentoInsereBanco(idCliente,dataInicio,dataFim):

	#iniciando variaveis
	controlador = True
	contadorPagamento= 0
	pagina = 1

	while controlador:


		link = "http://transparencia.portalfacil.com.br/api/pagamentos?type=json&idCliente="+str(idCliente)+"&page="+str(pagina)+"&pageSize=100&dtInicio="+dataInicio+"&dtFim="+dataFim
		con = conectaBanco()
		listaEmpenhos = []
		try:
			r = requests.get(link)
			if r.status_code == 200:
				reddit_data = json.loads(r.content)
				if len(reddit_data)==21:
					print("FIM DE RECUPERACAO DE PAGAMENTOS")
					return


				for reddit in reddit_data:
					try:
						pagamento = Pagamento.Pagamento(
							reddit['NumPagamento'],
							reddit['DtPagamento'],
							reddit['VlPagamento'],
							reddit['NumEmpenho']
						)


						cursor = con.cursor()
						#RETORNA O ID DO EMPENHO RELACIONADO AO PAGAMENTO
						cursor.execute("SELECT idEmpenho from Empenho where NumeroEmpenho = "+pagamento.numEmpenho+" AND idCliente = "+str(idCliente))
						retorno = cursor.fetchone()
						if(retorno != None):
							idEmpenho = str(retorno['idEmpenho'])

						#INSERINDO NO BANCO DE DADOS
						sqlquery = "INSERT INTO Pagamento(NumeroPagamento,DataPagamento,ValorPagamento,NumeroEmpenho,idCliente,idEmpenho) VALUES (%s, %s, %s, %s, %s, %s);"
						data  = datetime.strptime(pagamento.dataPagamento, "%d/%m/%Y").strftime("%Y-%m-%d")

						cursor.execute(sqlquery, (
						pagamento.numero,
						data,
						pagamento.valorPagamento,
						pagamento.numEmpenho,
						str(idCliente),
						str(idEmpenho)
						))

						con.commit()
						contadorPagamento = contadorPagamento + 1
						print("Pagamento {}".format (contadorPagamento))
						sys.stdout.write("\033[F")
						time.sleep(0.1)

					except :
						print("Erro Pagamento")
			pagina = pagina + 1
		except:
			print("ERRO DE CONEXÃO PAGAMENTO")

		#return

	con.close()

def limpaDadosBanco(nomeTabela):
	con = conectaBanco()
	cursor = con.cursor()

	sqlquery = "SET FOREIGN_KEY_CHECKS = 0;"
	cursor.execute(sqlquery)
	con.commit()

	sqlquery = "TRUNCATE "+nomeTabela+";"
	cursor.execute(sqlquery)
	con.commit()
	print("DADOS DA TABELA "+nomeTabela+" EXCLUIDOS")
	con.close()

#retorna lista de clientes adicionados no banco
def retornaClientes():
	listaClientes = []
	con = conectaBanco()
	cursor = con.cursor()

	cursor.execute("SELECT * from Cliente")

	while True:
		retorno = cursor.fetchone()
		if(retorno == None):
			break
		listaClientes.append(Cliente.Cliente(retorno['idCliente'],retorno['nome']))

	con.close()
	return listaClientes

#verifica se clientes retornam empenhos
#retorna lista de clientes que nao retorna empenhos pela api
def verificaSeRetornaEmpenho():
	listaClientes = retornaClientes()
	listaClientesSemEmpenho = []
	for cliente in listaClientes:

		idCliente = cliente.idcliente
		print(idCliente)
		link = "http://transparencia.portalfacil.com.br/api/empenhos?type=json&idCliente="+str(idCliente)+"&page=1&pageSize=100&dtInicio=01/01/2017&dtFim=31/12/2017"
		try:
			r = requests.get(link)
			reddit_data = json.loads(r.content)
			if(reddit_data=="Erro: Contate o Administrador do Sistema!"):
				listaClientesSemEmpenho.append(cliente)
		except ConnectionError as err:
			print(err)
	return listaClientesSemEmpenho
