class Favorecido(object):

    def __init__(self, Nome, CPF_CNPJ,Cargo):
        self.Nome = str(Nome)
        self.CPF_CNPJ = str(CPF_CNPJ)
        self.Cargo = str(Cargo)

    def retornaNome(self):
        return str(self.Nome)

    def retornaCPF_CNPJ(self):
        return str(self.CPF_CNPJ)

    def retornaCargo(self):
        return str(self.Cargo)