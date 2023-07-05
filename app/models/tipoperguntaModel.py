class TipoPergunta:
    def __init__(self, idtipopergunta, nometipopergunta, descriçãopergunta):
        self.idtipopergunta = idtipopergunta
        self.nometipopergunta = nometipopergunta
        self.descriçãopergunta = descriçãopergunta

    #encapsulamento idtipopergunta
    def get_idtipopergunta(self):
        return self.idtipopergunta
    def set_idtipopergunta(self, new_idtipopergunta):
        self.idtipopergunta = new_idtipopergunta

    #encapsulamento nometipopergunta
    def get_nometipopergunta(self):
        return self.nometipopergunta
    def set_nometipopergunta(self, new_nometipopergunta):
        self.nometipopergunta = new_nometipopergunta

    #encapsulamento descriçãopergunta
    def get_descriçãopergunta(self):
        return self.descriçãopergunta
    def set_descriçãopergunta(self, new_descriçãopergunta):
        self.descriçãopergunta = new_descriçãopergunta