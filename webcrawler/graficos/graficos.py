__author__ = "Gustavo Almeida"
import pandas as pd
import pymysql.cursors
import matplotlib.pyplot as plt


con = pymysql.connect(host = '127.0.0.1',
                      	      user = '*****',
                              passwd='*****',
                              db = 'Prefeitura',
                              cursorclass=pymysql.cursors.DictCursor
                              )



class GeraGraficos (object):
	def GeraGraficoDivisaoTotal(self,Divisao):

		
		if (Divisao == "Elemento"):
			TamSub = 12
		else:
			TamSub = 5
			

		with con.cursor() as cursor:

			cursor.execute("SELECT REPLACE(SUBSTRING("+str(Divisao)+",1,"+str(TamSub)+"),'-','') AS "+str(Divisao)+", SUM(Valor) AS Soma FROM Empenho GROUP BY "+str(Divisao)+" ORDER BY Soma DESC;")
			dados = cursor.fetchall()
			#print (dados)

		df = pd.DataFrame(dados)
		print (df)


		#df.plot('Orgao','Soma',kind='bar')
		
		df.plot(Divisao,'Soma',kind='bar',rot=10,lw=2,colormap='jet',figsize=(12,6),title="Gastos Por "+str(Divisao))
		plt.yscale('log')
		plt.ylabel("VALOR R$")
		plt.xlabel ("Tipo de "+str(Divisao))
		plt.grid(True)
		
		plt.show()


	def GeraGraficoPagamentoPorMes(self):

		with con.cursor() as cursor:

			cursor.execute("SET @row_number = 0;")
			cursor.execute("SELECT (@row_number:=@row_number + 1) AS mes, SUM(ValorPagamento) AS ValorPago FROM Pagamento GROUP BY MONTH(DataPagamento) ORDER BY MONTH(DataPagamento);")
			dados = cursor.fetchall()
			#print (dados)

		df = pd.DataFrame(dados)
		df.plot('mes','ValorPago',kind='bar',colormap='jet',figsize=(10,4),title='Valores Pagos pela Prefeitura')
		plt.yscale('log')
		#df.plot('DataPagamento','ValorPago',color='C2')
		#plt.title("Valores Pagos pela Prefeitura")
		plt.ylabel("VALOR R$")
		plt.xlabel ("MÊS")
		plt.grid(True)

		plt.show()


	def GeraHistogramaDePagamentos(self):

		with con.cursor() as cursor:

			
			cursor.execute("SELECT Nome, SUM(ValorPagamento) AS soma FROM (Favorecido NATURAL JOIN Empenho) NATURAL JOIN Pagamento GROUP BY IdFavorecido;")
			dados = cursor.fetchall()
			

		df = pd.DataFrame(dados)
		df.plot('Nome','soma',kind='hist',title='Pagamentos aos Favorecidos: HISTOGRAMA')
		plt.yscale('log')
		#df.plot('DataPagamento','ValorPago',color='C2')
		#plt.title("Valores Pagos pela Prefeitura")
		plt.ylabel("VALOR R$")
		#plt.xlabel ("TOTAL PAGO")
		plt.grid(True)

		plt.show()

	def GeraGraficoValorEmpenhadoEPago(self):

		with con.cursor() as cursor:

			
			cursor.execute("SELECT Orgao, SUM(Valor) AS ValorEmpenhado, SUM(ValorPagamento) AS ValorPago From (Empenho Natural join Pagamento) GROUP BY Orgao ORDER BY ValorEmpenhado;")
			dados = cursor.fetchall()
			

		df = pd.DataFrame(dados)
		print(dados)
		df.plot(x='Orgao',kind='barh',title="Valores Empenhados e Valores Pagos")
		plt.xscale('log')
		#df.plot('DataPagamento','ValorPago',color='C2')
		#plt.title("Valores Pagos pela Prefeitura")
		plt.ylabel("VALOR R$")
		plt.xlabel ("Data do Pagamento")
		plt.grid(True)

		plt.show()

	def GeraGraficoDivisaoPagoEEpenhado(self, Divisao):


		with con.cursor() as cursor:

			if (Divisao == "Elemento"):
				TamSub = 12
			else:
				TamSub = 5


			cursor.execute("Select REPLACE(SUBSTRING("+str(Divisao)+",1,"+str(TamSub)+"),'-','') AS "+str(Divisao)+", ValorPago, ValorEmpenhado FROM (Select REPLACE(SUBSTRING("+str(Divisao)+",1,"+str(TamSub)+"),'-','') AS "+str(Divisao)+",SUM(ValorPagamento) ValorPago From Favorecido Natural Join Empenho Natural Join Pagamento GROUP BY "+str(Divisao)+") T JOIN (Select REPLACE(SUBSTRING("+str(Divisao)+",1,"+str(TamSub)+"),'-','') AS "+str(Divisao)+"2, SUM(Valor) ValorEmpenhado From Empenho GROUP BY "+str(Divisao)+") T2 ON T."+str(Divisao)+" = T2."+str(Divisao)+"2 ORDER BY ValorPago DESC;")
			dados = cursor.fetchall()
			
			

		df = pd.DataFrame(dados)
		#(df)
		df.plot(x=Divisao,kind ='bar',figsize=(12,6),title="Valores Pagos Por "+str(Divisao))
		plt.yscale('log')
		plt.ylabel("VALOR R$")
		plt.xlabel ("Tipo de "+str(Divisao))
		plt.grid(True)
		
		plt.show()

	def GeraGraficoGastosPorPessoa(self, ValorMinimo):


		with con.cursor() as cursor:

			cursor.execute("SELECT soma, Nome FROM (SELECT Nome, SUM(ValorPagamento) AS soma FROM (Favorecido NATURAL JOIN Empenho) NATURAL JOIN Pagamento GROUP BY IdFavorecido) tab Where soma >" +str(ValorMinimo)+" ORDER BY soma;")
			dados = cursor.fetchall()
			
			

		df = pd.DataFrame(dados)
		df.plot(x='Nome',y='soma',kind ='barh',align='center',figsize=(10,6),title="Valores pagos para favorecidos, com valor maior de R$ "+str(ValorMinimo))
		plt.xscale('log')
		plt.xlabel ("Valor Pago")
		plt.grid(True)
		plt.show()

	def GeraGraficoGastosPorCargo(self):


		with con.cursor() as cursor:

			cursor.execute("SELECT  Distinct(Cargo) AS Cargo, Sum(ValorPagamento) As Soma FROM (Favorecido NATURAL JOIN Empenho) NATURAL JOIN Pagamento GROUP BY Cargo Order By Soma ASC;")
			dados = cursor.fetchall()
			
			

		df = pd.DataFrame(dados)
		df.plot(x='Cargo',y='Soma',kind ='barh',figsize=(20,10),title="Valores pagos por Cargo")
		
		plt.xlabel ("Valor Pago")
		
		plt.show()


	def GeraGraficoPagamentoTotalAno(self):


		with con.cursor() as cursor:

			cursor.execute("SELECT SUM(ValorPagamento) Total2017 From Pagamento")
			dados = cursor.fetchall()
			
			

		df = pd.DataFrame(dados)
		df.plot(y='Total2017',kind ='pie',figsize=(10,6),title="")
		
		plt.xlabel ("")
		
		plt.show()
		

	def GeraGraficoValoresEmpenhados(self, ValorMinimo):


		with con.cursor() as cursor:

			cursor.execute("SELECT soma, Nome FROM (SELECT Nome, SUM(Valor) AS soma FROM (Favorecido NATURAL JOIN Empenho) NATURAL JOIN Pagamento GROUP BY IdFavorecido) tab Where soma >" +str(ValorMinimo))
			dados = cursor.fetchall()
			
			

		df = pd.DataFrame(dados)
		df.plot(x='Nome',y='soma',kind ='barh',align='center',figsize=(10,6),title="Valores Empenhados, com valor maior de R$ "+str(ValorMinimo))
		
		plt.xlabel ("Valor Empenhado")
		
		plt.show()

	def GeraGraficoValorPagoPorCargo(self):

		with con.cursor() as cursor:

			
			cursor.execute(" Select Cargo, SUM(ValorPagamento) AS ValorPago FROM (Favorecido Natural join Empenho) Natural Join Pagamento Group By Cargo Order By ValorPago;")
			dados = cursor.fetchall()
			

		df = pd.DataFrame(dados)
		df.plot(x='Cargo',y='ValorPago',kind='barh',title="Valores Pagos por Cargo - ESCALA LOG")
		plt.xscale('log')
		#df.plot('DataPagamento','ValorPago',color='C2')
		#plt.title("Valores Pagos pela Prefeitura")
		plt.ylabel("Nome do Cargo")
		plt.xlabel ("Valor pago")
		plt.grid(True)

		plt.show()
		


	




class PesquisaPorNumeroDoPagamento(object):

	def Pesquisa(self):
		pagamento = input ("entre com o Numero do empenho para pesquisa: ")
		with con.cursor() as cursor:
			cursor.execute("select DISTINCT (Nome) from ((Favorecido NATURAL JOIN Empenho) NATURAL JOIN Pagamento) where Numero = "+pagamento);
			nome = cursor.fetchall()
			if (nome.__len__() != 0):
				print ("O Pagamento número "+pagamento+" pertence ao favorecido: "+str((nome[0])['Nome']))
			else:
				print("Nenhum pagamento referente à entrada!")
			








c = GeraGraficos()
c.GeraGraficoPagamentoPorMes()
#c.GeraGraficoDivisaoPagoEEpenhado("SubFuncao")
#c.GeraHistogramaDePagamentos()

#c.GeraGraficoDivisaoPagamentos("Elemento")
#c.GeraGraficoGastosPorPessoa(10000)
#c.GeraGraficoValoresEmpenhados(8000)
#c.GeraGraficoPagamentoTotalAno()
#c.GeraGraficoValorPagoPorCargo()

#d = PesquisaPorNumeroDoPagamento()
#d.Pesquisa()
