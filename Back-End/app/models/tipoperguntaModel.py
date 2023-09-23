class TipoPergunta:
    def __init__(self, id_tipo_pergunta, nome_tipo_pergunta):
        self._id_tipo_pergunta = id_tipo_pergunta
        self._nome_tipo_pergunta = nome_tipo_pergunta

    #encapsulamento id_tipo_pergunta
    def get_id_tipo_pergunta(self):
        return self._id_tipo_pergunta
    def set_id_tipo_pergunta(self, new_id_tipo_pergunta):
        self._id_tipo_pergunta = new_id_tipo_pergunta

    #encapsulamento nome_tipo_pergunta
    def get_nome_tipo_pergunta(self):
        return self._nome_tipo_pergunta
    def set_nome_tipo_pergunta(self, new_nome_tipo_pergunta):
        self._nome_tipo_pergunta = new_nome_tipo_pergunta