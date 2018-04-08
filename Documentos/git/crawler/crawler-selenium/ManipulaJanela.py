from selenium import webdriver
import time
import dados
import os

Empenhos = []
Anulacoes = []
Complementos = []


# EXCLUSIVO PARA "TABLES": retorna a quantidade de subtabelas da tabela original.
# Como as opcões são todas iguais, verificar erros individuais seria dificil. try-except auxilia nessa abordagem, sem qualquer outro teste adicional
# Os botões das tabelas possuem uma quntidade limitada de opções, que, dinamicamente, tornam-se links para valores diferentes.
def RetornaQuantidadeDePaginas(driver):
    time.sleep(2)

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
                        Num_Paginas = int(
                            driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[3]/a').text)
                    except:
                        try:
                            Num_Paginas = int(
                                driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[2]/a').text)
                        except:
                            try:
                                Num_Paginas = int(
                                    driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[1]/a').text)
                            except:
                                Num_Paginas = int(
                                    driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[0]/a').text)
    # print("Numero de paginas: "+str(Num_Paginas))
    return int(Num_Paginas)


def CapturaListaDePagamentos(driver):
    indiceDespesa = 0
    ListaDespesa = []

    while (True):
        indiceDespesa = indiceDespesa + 1
        try:

            time.sleep(2)

            des = driver.find_element_by_xpath(('//*[@id="datatablePagamentos"]/tbody/tr[' + str(indiceDespesa) + ']'))
            ListaDespesa.append(des.text)

        except:
            return list(ListaDespesa)


def CapturaTabelaDeEmpenhos(driver):
    Num_Paginas = RetornaQuantidadeDePaginas(driver)
    Quant_pagina = 0

    i = 1

    while (Quant_pagina < Num_Paginas):

        NavegaTabelas(driver, Quant_pagina, Num_Paginas)

        for x in range(10):

            path_empenho = '//table[@id="datatable"]/tbody/tr[' + str(x + 1) + ']/td[1]/a'

            try:

                time.sleep(2)

                empenho = driver.find_element_by_xpath(path_empenho)



            except:
                # print("\nFim dos empenhos!\n")
                break

            empenho.click()
            time.sleep(2)

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
            Favorecido = Favorecido.replace("Favorecido: ", "")

            print (Favorecido)

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

            emp = dados.Empenho(Num_Empenho, Especie, Orgao, ProjetoAtvAcao, ElementoDespesa, Licitacao, NumProcesso,
                                DataEmpenho, ValorEmpenhado, Funcao, SubFuncao, Programa, Destinacao)
            emp.InsereFavorecido(Favorecido, CPF_CNPJ, Cargo)

            # Validação e garantia da sequencia. Implementação com Curto Circuito
            if (((Empenhos.__len__() != 0)) and (
                    Favorecido < ((Empenhos[Empenhos.__len__() - 1])).RetornaFavorecido().Nome)):
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

            if (emp.Especie == "Anulacao"):  # não armazenar anulações
                Anulacoes.append(emp)
            elif (emp.Especie == "Complementar"):  # não armazenar complementos

                Complementos.append(emp)
            elif ((emp.Especie == "Ordinario") & (emp.Pagamentos.__len__() == 0)):  # verificar se a anulação anula um ordinario integralmente
                if (Anulacoes.__len__() != 0):
                    if (emp.Numero == Anulacoes.pop().Numero):
                        Anulacoes = []
                else:
                    Empenhos.append(emp)
            elif ((emp.Especie == "Ordinario") & (Anulacoes.__len__() != 0)):  # diminuir valor anulado de um empenho vigente
                print ("removendo valor anulado")
                while (Anulacoes.__len__() != 0):
                    emp.Valor += Anulacoes.pop().Valor
                Empenhos.append(emp)

            elif ((emp.Especie == "Estimativo") & (Anulacoes.__len__() != 0)):  # diminuir valor anulado de um empenho vigente
                print ("removendo valor anulado")
                while(Anulacoes.__len__() != 0 ):
                    emp.Valor += Anulacoes.pop().Valor

                if (Complementos.__len__() != 0):
                    for comp in Complementos:
                        emp.Valor = float(emp.Valor) + float(comp.Valor)
                        Complementos = []
                Empenhos.append(emp)

            elif (((emp.Especie == "Estimativo")) & (
                    Complementos.__len__() != 0)):  # existem complementos pendentes para a especie atual

                for comp in Complementos:
                    emp.Valor = float(emp.Valor) + float(comp.Valor)
                Empenhos.append(emp)
                Complementos = []


            else:  # insere Ordinario e Estimativo
                Empenhos.append(emp)

            # verificar mais empenhos para capturar (da mesma pessoa)
            driver.back()
            NavegaTabelas(driver, Quant_pagina, Num_Paginas)
            time.sleep(2)
        Quant_pagina = Quant_pagina + 1


def NavegaTabelas(driver, IndiceAtual, QuantidadeTotalIndices):
    i = 1

    for x in range(IndiceAtual + 1):

        try:

            time.sleep(2)
            b = driver.find_element_by_xpath('//div[@id="datatable_paginate"]/ul/li[' + str(i) + ']/a')


        except:

            return

        b.click()
        # print("INDICE ATUAL:" + str(IndiceAtual))
        # print("TOTAL INDICES" + str(QuantidadeTotalIndices))

        # estamos na ultima pagina

        # naveganto nas primeiras opçoes. Sabendo que se trata de um 'vetor' com 6 posições com possibilidade  de escolha
        if (i <= 4):
            i = i + 1
        elif (x + 1 == QuantidadeTotalIndices - 2):  # penultima
            i += 1
        elif (x + 1 == QuantidadeTotalIndices - 1):  # ultima
            i += 1

        time.sleep(2)


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
