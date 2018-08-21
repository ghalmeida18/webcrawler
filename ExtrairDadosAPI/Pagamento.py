class Pagamento (object):

    def __init__(self, Numero, DataPagamento, ValorPagamento):
        self.Numero = int (Numero)
        self.DataPagamento = str(DataPagamento)
        self.ValorPagamento = ConverteValor(ValorPagamento)