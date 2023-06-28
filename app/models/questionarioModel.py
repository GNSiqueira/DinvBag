class Questionario:
    def __init__(self, idQuestionario, estagio, acertos):
        self._idquestionario = idQuestionario
        self._estagio = estagio
        self._acertos = acertos

    #encapsulamento idquestionario
    def get_idquestionatio(self):
        return self._idquestionario
    
    #encapsulamento estagio
    def get_estagio(self):
        return self._estagio
    def set_estagio(self, new_estagio):
        self._estagio = new_estagio

    #encapsulamento acertos
    def get_acertos(self):
        return self._acertos
    def set_acertos(self, new_acertos):
        self._acertos = new_acertos