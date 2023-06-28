class Pergunta:
    def __init__(self, idPergunta, textoPergunta, alt1, alt2, alt3, alt4, resposta, idTipoPergunta, idQuestionario):
        self._idpergunta = idPergunta
        self._textopergunta = textoPergunta
        self._alt1 = alt1
        self._alt2 = alt2
        self._alt3 = alt3
        self._alt4 = alt4
        self._resposta = resposta
        self._idtipopergunta = idTipoPergunta
        self._idquestionario = idQuestionario

    #encapsulamento idpergunta
    def get_idpergunta(self):
       return self._idpergunta
    
    #encápsulamento textopergunta
    def get_textopergunta(self):
        return self._textopergunta
    def set_textopergunta(self, new_textopergunta):
        self._textopergunta = new_textopergunta

    #encapsulamento alt1
    def get_alt1(self):
        return self._alt1
    def set_alt1(self, new_alt1):
        self._alt1 = new_alt1

    #encapsulamento alt2
    def get_alt2(self):
        return self._alt2
    def set_alt2(self, new_alt2):
        self._alt2 = new_alt2

    #encapsulamento alt3
    def get_alt3(self):
        return self._alt3
    def set_alt3(self, new_alt3):
        self._alt3 = new_alt3
    
    #encapsulamento alt4
    def get_alt4(self):
        return self._alt4
    def set_alt4(self, new_alt4):
        self._alt4 = new_alt4

    #encapsulamento resposta
    def get_resposta(self):
        return self._resposta
    def set_resposta(self, new_resposta):
        self._resposta = new_resposta

    #encapsulamento idtipopergunta
    def get_idtipopergunta(self):
        return self._idtipopergunta
    
    #encapsulamento idquestionario
    def get_idquestionario(self):
        return self._idquestionario
    