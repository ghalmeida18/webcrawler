import json
import requests
import pymysql.cursors
from datetime import datetime

import Cliente
import Empenho



def conectaBanco():
	con = pymysql.connect(host = '127.0.0.1',
                      	      user = 'root',
                              passwd='root',
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



def recuperaEmpenhoInsereBanco(idCliente):


	pagina = 0
	controlador = True

	contadorDeEmpenhos = 0

	while controlador:
		pagina = pagina + 1
		print(pagina)
		link = "http://transparencia.portalfacil.com.br/api/empenhos?type=json&idCliente="+str(idCliente)+"&page="+str(pagina)+"&pageSize=100&dtInicio=01/01/2018&dtFim=31/12/2018"
		#link = "http://transparencia.portalfacil.com.br/api/empenhos?type=json&idCliente="+str(idCliente)+"&page=21&pageSize=100&dtInicio=01/01/2018&dtFim=31/12/2018"
		con = conectaBanco()
		listaEmpenhos = []

		r = requests.get(link)
		if r.status_code == 200:
			reddit_data = json.loads(r.content)
			if len(reddit_data)==21:
				print("arroz")
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
						sqlquery = "INSERT INTO Favorecido(CPF_CNPJ, Nome, Cargo) VALUES (%s, %s, %s);"
						cursor.execute(sqlquery,(
						        empenho.retornaFavorecido().CPF_CNPJ,
						        empenho.retornaFavorecido().retornaNome(),
						        empenho.retornaFavorecido().retornaCargo()
						        ))
						con.commit()

					#RETORNA O ID DO FAVORECIDO ADICIONADO
					cursor.execute("SELECT IdFavorecido from Favorecido where Nome = '"+empenho.retornaFavorecido().retornaNome()+"'")
					IdRetornado = cursor.fetchone()
					idFavorecido = str(IdRetornado['IdFavorecido'])

					#INSERE EMPENHO
					sqlquery = "INSERT INTO Empenho(Especie,Orgao,Projeto,Elemento,Licitacao,Processo,DataEmpenho,Valor,Empenho_Numero,IdFavorecido,Funcao,SubFuncao,Programa,Destinacao,idCliente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

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
					contadorDeEmpenhos = contadorDeEmpenhos + 1
					print(contadorDeEmpenhos)
				except :
					print("Erro empenho")

		#return

	con.close()
