import json
import requests
import pymysql.cursors


con = pymysql.connect(host = '127.0.0.1',
                      	      user = 'root',
                              passwd='root',
                              db = 'testeXml',
                              cursorclass=pymysql.cursors.DictCursor
                              )



r = requests.get('http://transparencia.portalfacil.com.br/api/clientes?type=json')
if r.status_code == 200:
	reddit_data = json.loads(r.content)
	for reddit in reddit_data:
		try:
			sql = "INSERT INTO cidade(nome,idcidade) values ('"+reddit['DescCliente']+"',"+reddit['IdCliente']+")"
			cursor = con.cursor()
			cursor.execute(sql)
			con.commit()
			print(reddit['DescCliente']+" "+reddit['IdCliente'])
		except :
			print("Erro ao inserir cidade")

