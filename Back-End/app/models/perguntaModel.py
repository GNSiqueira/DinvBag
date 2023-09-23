class Pergunta:
    def __init__(self, id_pergunta, texto_pergunta, alternativa1, alternativa2, alternativa3, alternativa4, resposta_pergunta, id_tipo_pergunta):
        self._id_pergunta = id_pergunta
        self._texto_pergunta = texto_pergunta
        self._alternativa1 = alternativa1
        self._alternativa2 = alternativa2
        self._alternativa3 = alternativa3
        self._alternativa4 = alternativa4
        self._resposta_pergunta = resposta_pergunta
        self._id_tipo_pergunta = id_tipo_pergunta

    #encapsulamento id_pergunta
    def get_id_pergunta(self):
       return self._id_pergunta
    
    #encápsulamento texto_pergunta
    def get_texto_pergunta(self):
        return self._texto_pergunta
    def set_texto_pergunta(self, new_texto_pergunta):
        self._texto_pergunta = new_texto_pergunta

    #encapsulamento alternativa1
    def get_alternativa1(self):
        return self._alternativa1
    def set_alternativa1(self, new_alternativa1):
        self._alternativa1 = new_alternativa1

    #encapsulamento alternativa2
    def get_alternativa2(self):
        return self._alternativa2
    def set_alternativa2(self, new_alternativa2):
        self._alternativa2 = new_alternativa2

    #encapsulamento alternativa3
    def get_alternativa3(self):
        return self._alternativa3
    def set_alternativa3(self, new_alternativa3):
        self._alternativa3 = new_alternativa3
    
    #encapsulamento alternativa4
    def get_alternativa4(self):
        return self._alternativa4
    def set_alternativa4(self, new_alternativa4):
        self._alternativa4 = new_alternativa4

    #encapsulamento resposta_pergunta
    def get_resposta_pergunta(self):
        return self._resposta_pergunta
    def set_resposta_pergunta(self, new_resposta_pergunta):
        self._resposta_pergunta = new_resposta_pergunta

    #encapsulamento id_tipo_pergunta
    def get_id_tipo_pergunta(self):
        return self._id_tipo_pergunta