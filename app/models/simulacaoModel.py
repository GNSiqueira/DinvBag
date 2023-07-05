class Simulacao:
    def __init__(self, idsimulacao, datasimulacao, valor, datainicial, datafinal, retorno, acao, idusuario):
        self.idsimulacao = idsimulacao
        self.datasimulacao = datasimulacao
        self.valor = valor
        self.datainicial = datainicial
        self.datafinal = datafinal
        self.retorno = retorno
        self.acao = acao
        self.idusuario = idusuario
        
    #encapsulamento idsimulacao
    def get_idsimulacao(self):
        return self.idsimulacao
    def set_idsimulacao(self, new_idsimulacao):
        self.idsimulacao = new_idsimulacao  

    #encapsulamento datasimulacao
    def get_datasimulacao(self):
        return self.datasimulacao
    def set_datasimulacao(self, new_datasimulacao):
        self.datasimulacao = new_datasimulacao

    #encapsulamento valor
    def get_valor(self):
        return self.valor
    def set_valor(self, new_valor):
        self.valor = new_valor   

    #encapsulamento datainicial
    def get_datainicial(self):
        return self.datainicial
    def set_datainicial(self, new_datainicial):
        self.datainicial = new_datainicial   

    #encapsulamento datafinal
    def get_datafinal(self):
        return self.datafinal
    def set_datafinal(self, new_datafinal):
        self.datafinal = new_datafinal   

    #encapsulamento retorno
    def get_retorno(self):
        return self.retorno
    def set_retorno(self, new_retorno):
        self.retorno = new_retorno   

    #encapsulamento acao
    def get_acao(self):
        return self.acao
    def set_acao(self, new_acao):
        self.acao = new_acao    

    #encapsulamento idusuario
    def get_idusuario(self):
        return self.idusuario

