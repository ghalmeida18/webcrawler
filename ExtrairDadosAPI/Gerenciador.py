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

	link = "http://transparencia.portalfacil.com.br/api/empenhos?type=json&idCliente="+str(idCliente)+"&page=1&pageSize=100&dtInicio=01/01/2018&dtFim=31/12/2018"

	con = conectaBanco()
	
	listaEmpenhos = []
	r = requests.get(link)
	if r.status_code == 200:
		reddit_data = json.loads(r.content)
		for reddit in reddit_data:
			try:
				
				empenho = Empenho.Empenho()

				empenho.Especie = reddit['TpEmpenho']
				empenho.Orgao = reddit['NumUnidade']+" "+ reddit['DescUnidade']
				#empenho.Projeto = reddit['']#verifica
				empenho.Elemento =  reddit['NumDespesa']+" "+ reddit['DescDespesa']
				empenho.Licitacao = reddit['NumLicitacao']+" - "+reddit['DtLicitacao']+" - "+reddit['TpLicitacao']
				empenho.Processo = reddit['NumProcesso']

				empenho.DataEmpenho = reddit['DtEmpenho']
				print(empenho.Data)
				data  = datetime.strptime(empenho.Data,"%d/%m/%Y").strftime("%Y-%m-%d")
				print("2")

				empenho.Valor = reddit['VlEmpenho']
				empenho.Empenho_Numero = reddit['NumEmpenho']	

				empenho.Funcao = reddit['NumFuncao']+" - "+reddit['DescFuncao']
				empenho.SubFuncao = reddit['NumSubFuncao']+" - "+reddit['DescSubFuncao']
				empenho.Programa = reddit['NumPrograma']+" - "+reddit['DescPrograma']
				empenho.Destinacao = reddit['NumDestinacao']+" - "+reddit['DescDestinacao']
				empenho.IdCliente = idCliente


				print(empenho.Orgao)
				
				#cursor = con.cursor()
				#cursor.execute(sql)
				con.commit()
				#print(reddit['DescCliente']+" "+reddit['IdCliente'])
				
			except :
				print("Erro ao inserir Empenho")
	con.close()
