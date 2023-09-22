class TipoPergunta:
    def __init__(self, idtipopergunta, nometipopergunta, descriçãopergunta):
        self._idtipopergunta = idtipopergunta
        self._nometipopergunta = nometipopergunta
        self._descriçãopergunta = descriçãopergunta

    #encapsulamento idtipopergunta
    def get_idtipopergunta(self):
        return self._idtipopergunta
    def set_idtipopergunta(self, new_idtipopergunta):
        self._idtipopergunta = new_idtipopergunta

    #encapsulamento nometipopergunta
    def get_nometipopergunta(self):
        return self._nometipopergunta
    def set_nometipopergunta(self, new_nometipopergunta):
        self._nometipopergunta = new_nometipopergunta

    #encapsulamento descriçãopergunta
    def get_descriçãopergunta(self):
        return self._descriçãopergunta
    def set_descriçãopergunta(self, new_descriçãopergunta):
        self._descriçãopergunta = new_descriçãopergunta