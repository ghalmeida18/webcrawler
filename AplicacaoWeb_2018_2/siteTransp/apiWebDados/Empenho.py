from siteTransp.apiWebDados import Favorecido

class Empenho(object):

    favorecido =  ""
    pagamentos = []
    
    numero = None
    especie = None
    orgao = None
    projeto = None
    elemento = None
    licitacao = None
    processo = None
    data = None
    valor = None
    funcao = None
    subFuncao = None
    programa = None
    destinacao = None

    def insereFavorecido(self,nome, CPF_CNPJ, cargo):
        self.favorecido = Favorecido.Favorecido(nome, CPF_CNPJ, cargo)

    def retornaFavorecido(self):
        return (self.favorecido)

    def inserePagamento(self,numero, dataPagamento, valorPagamento):
        pg = pagamentos(numero, dataPagamento, valorPagamento)
        self.pagamentos.append(pg)

    def retornaPagamento(self):
        return self.pagamentos

    def apagaLista(self):
        self.pagamentos = []

    def listaEstaVazia(self):
        if (self.pagamentos.__len__() == 0):
            return True
        else:
            return False