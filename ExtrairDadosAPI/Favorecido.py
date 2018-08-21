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