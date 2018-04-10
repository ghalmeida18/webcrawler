__author__ = "Gustavo Almeida"
import datetime
from selenium import webdriver
import time
import dados
import ManipulaJanela


QuantidadeRegistros = 0

class CapturaDados(object):

    def __init__(self, address):
        self.ad = str(address)
        print ("\nIniciando análise... \n\n")

    def Inicia_Captura(self,PaginaDeInicio):
        driver = webdriver.Chrome("/home/gustavo/Documentos/chromedriver")
        driver.get(self.ad)


        cont = 1 #contador de nomes encontrados
        Quant_pagina = PaginaDeInicio #quantidades de páginas analisadas ate o momento.



        #Captura a quantidade de paginas total do site
        Num_Paginas = ManipulaJanela.RetornaQuantidadeDePaginas(driver)

        # nao utilizado. retorna quantidade total de registros
        QuantidadeRegistros = ManipulaJanela.RetornaQuantidadeDeRegistros(driver)




        while (  Quant_pagina < Num_Paginas ):

                    ManipulaJanela.NavegaTabelas(driver, Quant_pagina, Num_Paginas)
                    x = 0


                    # captura os 10 nomes presente na tabela da atual página até chegar na ultima, que pode ter <10
                    while x < 10:
                        x = x + 1
                        #print("FAVORECIDO NUMERO "+ str(x))

                        path_favorecido = '//table[@id="datatable"]/tbody/tr['+ str(x) +']/td[1]/a'


                        try:

                            time.sleep(2)
                            nome = driver.find_element_by_xpath(path_favorecido)



                        except:
                            print ("\nFim da análise: "+str(cont - 1)+" dados capturados!\n")
                            return


                        nome.click()#abre novos dados.



                        #erro na captura de dados. Possivelmente devido a conexao
                        try:
                            ManipulaJanela.CapturaTabelaDeEmpenhos(driver)
                        except:

                            print("ERRO! VERIFIQUE CONEXÂO. RECUPERANDO SISTEMA...")
                            driver.back()
                            time.sleep(2)
                            driver.back()
                            time.sleep(2)
                            ManipulaJanela.NavegaTabelas(driver, Quant_pagina, Num_Paginas)

                            x = x - 1
                            continue

                        driver.back()#volta para lista de favorecidos, tabelas.

                        ManipulaJanela.NavegaTabelas(driver, Quant_pagina, Num_Paginas)
                        time.sleep(2)# aguarda a execução do JS, 1 segundo

                        #ManipulaJanela.ImprimePorcentagem(cont,QuantidadeRegistros)

                        cont = cont + 1
                        
                        



                    #proxima pagina
                    Quant_pagina = Quant_pagina + 1
			  

                    #Para capturar apenas uma pagina, descomentar o return.
                    return






    def InserirDados(self):

        print("Inserindo dados no Banco de Dados prefeitura")
        BD = dados.InserirBD()
        BD.InserirDados(ManipulaJanela.Empenhos)

    def AtualizarDados(self):

        print("Atualizando dados no Banco de Dados prefeitura")
        BD = dados.AtualizarBD()
        BD.InserirDados(ManipulaJanela.Empenhos)








