class Resposta:
    def __init__(self, id_resposta, alternativa_respondida, alternativa_correta, data_resposta, id_questionario, id_pergunta):
        self._id_resposta = id_resposta
        self._alternativa_respondida = alternativa_respondida
        self._alternativa_correta = alternativa_correta
        self._data_resposta = data_resposta
        self._id_questionario = id_questionario
        self._id_pergunta = id_pergunta

    #encapsulamento id_resposta
    def get_id_respsota(self):
        return self._id_resposta
    
    #encapsulamento alternativa_respondida
    def get_alternativa_respondida(self):
        return self._alternativa_respondida
    def set_alternativa_respondida(self, new_alternativa_respondida):
        self._alternativa_respondida = new_alternativa_respondida

    #encapsulamento alternativa_correta
    def get_alternativa_correta(self):
        return self._alternativa_correta
    def set_alternativa_correta(self, new_alternativa_correta):
        self._alternativa_correta = new_alternativa_correta
    
    #encapsulamento data_resposta
    def get_data_resposta(self):
        return self._data_resposta
    def set_data_resposta(self, new_data_resposta):
        self._data_resposta = new_data_resposta

    #encapsulamento id_questionario
    def get_id_questionario(self):
        return self._id_questionario
    def set_id_questionario(self, new_id_questionario):
        self._id_questionario = new_id_questionario

    #encapsulamento id_pergunta
    def get_id_pergunta(self):
        return self._id_pergunta
    def set_id_pergunta(self, new_id_pergunta):
        self._id_pergunta = new_id_pergunta