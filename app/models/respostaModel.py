class Resposta:
    def __init__(self, idresposta, descricaoresposta, alternativacorreta, datapergunta, idusuario, idpergunta):
        self._idresposta = idresposta
        self._descricaoresposta = descricaoresposta
        self._alternativacorreta = alternativacorreta
        self._datapergunta = datapergunta
        self._idusuario = idusuario
        self._idpergunta = idpergunta

    #encapsulamento idresposta
    def get_idrespsota(self):
        return self._idresposta
    
    #encapsulamento descricaoresposta
    def get_descricaoresposta(self):
        return self._descricaoresposta
    def set_descricaoresposta(self, new_descricaoresposta):
        self._descricaoresposta = new_descricaoresposta

    #encapsulamento alternativacorreta
    def get_alternativacorreta(self):
        return self._alternativacorreta
    def set_alternativacorreta(self, new_alternativacorreta):
        self._alternativacorreta = new_alternativacorreta
    
    #encapsulamento datapergunta
    def get_datapergunta(self):
        return self._datapergunta
    def set_datapergunta(self, new_datapergunta):
        self._datapergunta = new_datapergunta

    #encapsulamento idusuario
    def get_idusuario(self):
        return self._idusuario
    def set_idusuario(self, new_idusuario):
        self._idusuario = new_idusuario

    #encapsulamento idpergunta
    def get_idpergunta(self):
        return self._idpergunta
    def set_idpergunta(self, new_idpergunta):
        self._idpergunta = new_idpergunta