class Questionario:
    def __init__(self, id_questionario, fase_questionario, acertos_questionario, id_usuario):
        self._id_questionario = id_questionario
        self._estagio_questionario = fase_questionario
        self._acertos_questionario = acertos_questionario
        self._id_usuario = id_usuario

    #encapsulamento id_questionario
    def get_id_questionatio(self):
        return self._id_questionario
    
    #encapsulamento fase_questionario
    def get_fase_questionario(self):
        return self._fase_questionario
    def set_fase_questionario(self, new_fase_questionario):
        self._fase_questionario = new_fase_questionario

    #encapsulamento acertos_questionario
    def get_acertos_questionario(self):
        return self._acertos_questionario
    def set_acertos_questionario(self, new_acertos_questionario):
        self._acertos_questionario = new_acertos_questionario

    #encapsulamento id_usuario
    def get_id_usuario(self):
        return self._id_usuario