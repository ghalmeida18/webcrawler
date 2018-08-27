import datetime
from enum import Enum
import pymysql.cursors
from datetime import datetime

class Favorecido(object):

    def __init__(self, Nome, CPF_CNPJ,Cargo):
        self.Nome = str(Nome)
        self.CPF_CNPJ = str(CPF_CNPJ)
        self.Cargo = str(Cargo)

    def RetornaNome(self):
        return str(self.Nome)

    def RetornaCPF_CNPJ(self):
        return str(self.CPF_CNPJ)

    def RetornaCargo(self):
        return str(self.Cargo)



class Empenho(object):

    Favorecido =  ""
    Pagamentos = []

    def __init__(self, Numero, Especie, Orgao, Projeto, Elemento, Licitacao, Processo, Data, Valor,Funcao,SubFuncao,Programa,Destinacao):
        self.Numero = Numero #chave
        self.Especie = Especie
        self.Orgao = Orgao
        self.Projeto = Projeto
        self.Elemento = Elemento
        self.Licitacao = Licitacao
        self.Processo = Processo
        self.Data = str(Data)
        self.Valor = ConverteValor(Valor)
        self.Funcao = str(Funcao)
        self.SubFuncao = str(SubFuncao)
        self.Programa = str(Programa)
        self.Destinacao = str(Destinacao)


    def InsereFavorecido(self,Nome, CPF_CNPJ, Cargo):
        self.Favorecido = Favorecido(Nome, CPF_CNPJ, Cargo)

    def RetornaFavorecido(self):
        return (self.Favorecido)

    def InserePagamento(self,Numero, DataPagamento, ValorPagamento):
        pg = Pagamentos(Numero, DataPagamento, ValorPagamento)
        self.Pagamentos.append(pg)

    def RetornaPagamento(self):
        return self.Pagamentos

    def ApagaLista(self):
        self.Pagamentos = []

    def ListaEstaVazia(self):
        if (self.Pagamentos.__len__() == 0):
            return True
        else:
            return False


class Pagamentos (object):



    def __init__(self, Numero, DataPagamento, ValorPagamento):
        self.Numero = int (Numero)
        self.DataPagamento = str(DataPagamento)
        self.ValorPagamento = ConverteValor(ValorPagamento)






def ConverteValor(valor):
    return float(str(valor).replace(".","").replace("R$","").replace(",","."))


def ComparaDados(emp1,emp2):
    if(emp1.Numero == emp2.Numero):#ja existe esse Empenho
        return True
    else:
        return False


class InserirBD (object):
    def InserirDados(self,Empenhos):
        con = pymysql.connect(host = '127.0.0.1',
                      	      user = '****',
                              passwd='*******',
                              db = 'Prefeitura',
                              cursorclass=pymysql.cursors.DictCursor
                              )





        for emp in Empenhos:





                try:

                    with con.cursor() as cursor:


                        (cursor.execute( "SELECT * from Favorecido where Nome = '" + emp.RetornaFavorecido().RetornaNome() + "'"))
                        if  (not(cursor.execute( "SELECT * from Favorecido where Nome = '" + emp.RetornaFavorecido().RetornaNome() + "'"))):
                            sqlquery = "INSERT INTO Favorecido(CPF_CNPJ, Nome, Cargo) VALUES (%s, %s, %s);"
                            cursor.execute(sqlquery,(
                                    emp.RetornaFavorecido().CPF_CNPJ,
                                    emp.RetornaFavorecido().RetornaNome(),
                                    emp.RetornaFavorecido().RetornaCargo()
                                    ))

                            con.commit()

                        cursor.execute("SELECT IdFavorecido from Favorecido where Nome = '"+emp.RetornaFavorecido().RetornaNome()+"'")
                        IdRetornado = cursor.fetchone()
                        id = str(IdRetornado['IdFavorecido'])
                        #print(str(id))

                        #print(str(emp.Data))
                        data  = datetime.strptime(emp.Data,"%d/%m/%Y").strftime("%Y-%m-%d")
                        #print(str(data))



                        sqlquery = "INSERT INTO Empenho(Especie,Orgao,Projeto,Elemento,Licitacao,Processo,DataEmpenho,Valor,Empenho_Numero,IdFavorecido,Funcao,SubFuncao,Programa,Destinacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        cursor.execute(sqlquery,(
                            emp.Especie,
                            emp.Orgao,
                            emp.Projeto,
                            emp.Elemento,
                            emp.Licitacao,
                            emp.Processo,
                            data,
                            emp.Valor,
                            emp.Numero,
                            id,
                            emp.Funcao,
                            emp.SubFuncao,
                            emp.Programa,
                            emp.Destinacao
                            ))

                        con.commit()
                        #print("Entrou no emp")

                        pagamentos = emp.RetornaPagamento()
                        for pag in pagamentos:
                            #print("Entrou no pagamento")
                            sqlquery = "INSERT INTO Pagamento(Numero,DataPagamento,ValorPagamento,Empenho_Numero) VALUES (%s, %s, %s, %s);"

                            data  = datetime.strptime(pag.DataPagamento, "%d/%m/%Y").strftime("%Y-%m-%d")


                            cursor.execute(sqlquery, (
                                pag.Numero,
                                data,
                                pag.ValorPagamento,
                                emp.Numero
                            )
                            )
                        con.commit()
                        #print("Saiu no pagamento")
                except:
                    continue




class AtualizarBD(object):
    def InserirDados(self, Empenhos):
        con = pymysql.connect(host='127.0.0.1',
                              user='***',
                              passwd='******',
                              db='Prefeitura',
                              cursorclass=pymysql.cursors.DictCursor
                              )

        for emp in Empenhos:



            with con.cursor() as cursor:

                (cursor.execute("SELECT * from Favorecido where Nome = '" + emp.RetornaFavorecido().RetornaNome() + "'"))
                if (not (cursor.execute("SELECT * from Favorecido where Nome = '" + emp.RetornaFavorecido().RetornaNome() + "'"))):
                    sqlquery = "INSERT INTO Favorecido(CPF_CNPJ, Nome, Cargo) VALUES (%s, %s, %s);"
                    cursor.execute(sqlquery, (
                        emp.RetornaFavorecido().CPF_CNPJ,
                        emp.RetornaFavorecido().RetornaNome(),
                        emp.RetornaFavorecido().RetornaCargo()
                        ))

                    con.commit()
                    print ("Favorecido Atualizado!!")





                if (not (cursor.execute("SELECT IdFavorecido from Favorecido where Nome = '" + emp.RetornaFavorecido().RetornaNome() + "'"))):
                    IdRetornado = cursor.fetchone()
                    id = str(IdRetornado['IdFavorecido'])

                    data = datetime.strptime(emp.Data, "%d/%m/%Y").strftime("%Y-%m-%d")


                    sqlquery = "INSERT INTO Empenho(Especie,Orgao,Projeto,Elemento,Licitacao,Processo,DataEmpenho,Valor,Empenho_Numero,IdFavorecido,Funcao,SubFuncao,Programa,Destinacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                    cursor.execute(sqlquery, (
                        emp.Especie,
                        emp.Orgao,
                        emp.Projeto,
                        emp.Elemento,
                        emp.Licitacao,
                        emp.Processo,
                        data,
                        emp.Valor,
                        emp.Numero,
                        id,
                        emp.Funcao,
                        emp.SubFuncao,
                        emp.Programa,
                        emp.Destinacao
                    ))

                    con.commit()
                    print ("Empenho Atualizado!!")


            

            

                Pagamentos = emp.RetornaPagamento()
                for pag in Pagamentos:

                    if (not (cursor.execute("SELECT * from Pagamento where Numero = '"+str(pag.Numero)+"'"))):

                        sqlquery = "INSERT INTO Pagamento(Numero,DataPagamento,ValorPagamento,Empenho_Numero) VALUES (%s, %s, %s, %s);"

                        data = datetime.strptime(pag.DataPagamento, "%d/%m/%Y").strftime("%Y-%m-%d")

                        cursor.execute(sqlquery, (
                            pag.Numero,
                            data,
                            pag.ValorPagamento,
                            emp.Numero
                        )
                        )
                        con.commit()
                        print ("Pagamento Atualizado!!")




