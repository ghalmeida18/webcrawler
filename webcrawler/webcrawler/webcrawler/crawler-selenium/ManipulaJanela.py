__author__ = "Gustavo Almeida"
from selenium import webdriver
import time
import dados
import os
#import InserirBD


def tempo():
	time.sleep(1)
def BuscaMaisEmpenhos(driver, Quant_pagina, Num_Paginas):
	driver.back()
	NavegaTabelas(driver, Quant_pagina, Num_Paginas)
	tempo()
	

Empenhos = []
Anulacoes = []
Complementos = []


# EXCLUSIVO PARA "TABLES": retorna a quantidade de subtabelas da tabela original.
# Como as opcões são todas iguais, verificar erros individuais seria dificil. try-except auxilia nessa abordagem, sem qualquer outro teste adicional
# Os botões das tabelas possuem uma quntidade limitada de opções, que, dinamicamente, tornam-se links para valores diferentes.
def RetornaQuantidadeDePaginas(driver):
	tempo()

	try:
		Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[7]/a').text)
	except:
		try:
			Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[6]/a').text)
		except:
			try:
				Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[5]/a').text)
			except:
				try:
					Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[4]/a').text)
				except:
					try:
						Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[3]/a').text)
					except:
						try:
							Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[2]/a').text)
						except:
							try:
								Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[1]/a').text)
							except:
								Num_Paginas = int(driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[0]/a').text)
    # print("Numero de paginas: "+str(Num_Paginas))
	return int(Num_Paginas)


def CapturaListaDePagamentos(driver):
	indiceDespesa = 0
	ListaDespesa = []

	while (True):
		indiceDespesa = indiceDespesa + 1
		try:
			tempo()
			des = driver.find_element_by_xpath(('//*[@id="datatablePagamentos"]/tbody/tr[' + str(indiceDespesa) + ']'))
			ListaDespesa.append(des.text)
		except:
			return list(ListaDespesa)


def CapturaTabelaDeEmpenhos(driver):
	Num_Paginas = RetornaQuantidadeDePaginas(driver)

	#mudar para 0 
	# variavel para iniciar na enésima tabela de empenho. Lembre-se: N = (Indice - 1)
	Quant_pagina = 0

	i = 3

	while (Quant_pagina < Num_Paginas):

		NavegaTabelas(driver, Quant_pagina, Num_Paginas)
		for x in range(10):
			path_empenho = '//table[@id="datatable"]/tbody/tr[' + str(x + 1)+ ']/td[1]/a'
			try:
				tempo()
				empenho = driver.find_element_by_xpath(path_empenho)
			except:
				break

			empenho.click()
			tempo()

			Funcao = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[3]')).text
			Funcao = Funcao.replace("Função:", "")

			SubFuncao = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[4]')).text
			SubFuncao = SubFuncao.replace("SubFunção:", "")

			Programa = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[5]')).text
			Programa = Programa.replace("Programa:", "")

			Destinacao = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[8]')).text
			Destinacao = Destinacao.replace("Destinação:", "")

			Cargo = (driver.find_element_by_xpath('//*[@id="fornecedor"]/div/ul/li[2]')).text
			Cargo = Cargo.replace("Cargo:", "")

			CPF_CNPJ = (driver.find_element_by_xpath('//*[@id="fornecedor"]/div/ul/li[1]')).text
			CPF_CNPJ = CPF_CNPJ.replace("CPF/CNPJ: ", "")

			Favorecido = (driver.find_element_by_xpath('//*[@id="fornecedor"]/div/div')).text
			Favorecido = Favorecido.replace("Fornecedor: ", "")


			ValorEmpenhado = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[12]')).text
			ValorEmpenhado = ValorEmpenhado.replace("Valor Empenho:", "")

			DataEmpenho = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[11]')).text
			DataEmpenho = DataEmpenho.replace("Data Empenho: ", "")

			NumProcesso = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[10]')).text
			NumProcesso = NumProcesso.replace("Nº Processo Adm.:", "")

			Licitacao = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[9]')).text
			Licitacao = Licitacao.replace("Licitação: ", "")

			ElementoDespesa = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[7]')).text
			ElementoDespesa = ElementoDespesa.replace("Elemento Despesa: ", "")

			ProjetoAtvAcao = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[6]')).text
			ProjetoAtvAcao = ProjetoAtvAcao.replace("Projeto Atividade/Ação: ", "")

			Orgao = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[2]')).text
			Orgao = Orgao.replace("Órgão: ", "")

			Especie = (driver.find_element_by_xpath('//*[@id="info"]/div/ul/li[1]')).text
			Especie = Especie.replace("Espécie: ", "")

			Num_Empenho = (driver.find_element_by_xpath('//*[@id="info"]/div/div')).text
			Num_Empenho = Num_Empenho.replace("Número Empenho: ", "")


			print ("Empenho número: "+ str(Num_Empenho)+" Nome: "+ Favorecido)

			emp = dados.Empenho(Num_Empenho, Especie, Orgao, ProjetoAtvAcao, ElementoDespesa, Licitacao, NumProcesso,DataEmpenho, ValorEmpenhado, Funcao, SubFuncao, Programa, Destinacao)
			emp.InsereFavorecido(Favorecido, CPF_CNPJ, Cargo)

            # Validação e garantia da sequencia. Implementação com Curto Circuito
			if (((Empenhos.__len__() != 0)) and (Favorecido < ((Empenhos[Empenhos.__len__() - 1])).RetornaFavorecido().Nome)):
				print (Favorecido + "é menor que " + ((Empenhos[Empenhos.__len__() - 1])).RetornaFavorecido().Nome)
                		# erro na captura sequencial!
				raise ("Erro de atualização!")

            # CapturaListaDePagamentos(driver)
			lista = CapturaListaDePagamentos(driver)
			emp.ApagaLista()

            # inserir valores da lista de pagamentos.
			for l in lista:
				if (l != "Nenhum registro encontrado"):
					d = str(l).split(" ")
					valor = d[2]
					if (valor[0] != '-'):  # não armazenar dados negativos já tratados.
						emp.InserePagamento(d[0], d[1], d[2])

			global Anulacoes
			global Complementos
			#a = True
		
			if (emp.Especie == "Anulacao"):  
				for temp in Empenhos:
					if (emp.Numero == temp.Numero): #existe um empenho a ser atualizado na lista. debitar valor anulado.
						temp.Valor = emp.Valor + temp.Valor
						del emp #apaga valor anulado desnecessario
				try:
					Anulacoes.append(emp)#empenho ainda nao encontrado para anular
					print("Anulaçao temporariamente salva")
					
				except:
					print("Anulação apagada!")
					BuscaMaisEmpenhos(driver, Quant_pagina, Num_Paginas)
					continue


			if (emp.Especie == "Complementar"): 
				for temp in Empenhos:
					if (emp.Numero == temp.Numero): #existe um empenho a ser atualizado na lista. debitar valor complementado.
						temp.Valor = emp.Valor + temp.Valor
						del emp
				try:
					Complementos.append(emp)#empenho ainda nao encontrado para anular
					print("Complemento temporariamente salvo")
				except:
					print("Complemento apagado!")
					BuscaMaisEmpenhos(driver, Quant_pagina, Num_Paginas)
					continue

			

			verificador = Anulacoes.__len__()
		
			if ((emp.Especie == "Ordinario" or emp.Especie == "Estimativo" or emp.Especie == "Global") & (verificador>0)): #Encontrado Ordinario para anular
				print("Validando Anulaçoes...")
				for temp in Anulacoes:
					emp.Valor = emp.Valor + temp.Valor
				if(emp.Valor != 0.00):
					Empenhos.append(emp)

				Anulacoes = []



			verificador = Complementos.__len__()
			if ((emp.Especie == "Ordinario" or emp.Especie == "Estimativo" or emp.Especie == "Global") & (verificador>0)): #Encontrado Ordinario para complementar
				print("Validando COmplementos...")
				for temp in Complementos:
					emp.Valor = emp.Valor + temp.Valor
				if(emp.Valor != 0.00):
					Empenhos.append(emp) 	

				Complementos = []

			elif (emp.Especie != "Anulacao" and emp.Especie != "Complementar"):
				Empenhos.append(emp)
			#BD = InserirBD.InserirBD()
			#BD.Inserir(emp)	
			
	




            # verificar mais empenhos para capturar (da mesma pessoa)
			BuscaMaisEmpenhos(driver, Quant_pagina, Num_Paginas)
			#driver.back()
			#NavegaTabelas(driver, Quant_pagina, Num_Paginas)
			#tempo()
		Quant_pagina = Quant_pagina + 1

		#apagar
		#return


def NavegaTabelas(driver, IndiceAtual, QuantidadeTotalIndices):
	i = 1

	for x in range(IndiceAtual + 1):
		try:
			time.sleep(2)
			b = driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[' + str(i) + ']/a')
		except:
			return
		b.click()
		if (i <= 4):
			i = i + 1
		elif (x + 1 == QuantidadeTotalIndices - 2):  # penultima
			i += 1
		elif (x + 1 == QuantidadeTotalIndices - 1):  # ultima
			i += 1

		tempo()


# para verificar se todos os registros foram capturados corretamente
def RetornaQuantidadeDeRegistros(driver):
	xpath = '//*[@id="datatable_info"]'
	b = driver.find_element_by_xpath(xpath)
	b = (b.text).split()
	return (int(b[6]))


def ImprimePorcentagem(QuantidadeCapturada, QuantidadeTotal):
	os.system("cls")
	porcentagem = 0

	porcentagem = float((100 * QuantidadeCapturada) / QuantidadeTotal)
	print ("Aguarde. " + str(porcentagem) + "% dos dados capturados...")
