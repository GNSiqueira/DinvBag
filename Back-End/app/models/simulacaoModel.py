class Simulacao:
    def __init__(self, id_simulacao, data_simulacao, valor_simulacao, data_ini_simulacao, data_fin_simulacao, retorno_simulacao, acao_simulacao, id_usuario):
        self._id_simulacao = id_simulacao
        self._data_simulacao = data_simulacao
        self._valor_simulacao = valor_simulacao
        self._data_ini_simulacao = data_ini_simulacao
        self._data_fin_simulacao = data_fin_simulacao
        self._retorno_simulacao = retorno_simulacao
        self._acao_simulacao = acao_simulacao
        self._id_usuario = id_usuario
        
    #encapsulamento id_simulacao
    def get_id_simulacao(self):
        return self._id_simulacao
    def set_id_simulacao(self, new_id_simulacao):
        self._id_simulacao = new_id_simulacao  

    #encapsulamento data_simulacao
    def get_data_simulacao(self):
        return self._data_simulacao
    def set_data_simulacao(self, new_data_simulacao):
        self._data_simulacao = new_data_simulacao

    #encapsulamento valor_simulacao
    def get_valor_simulacao(self):
        return self._valor_simulacao
    def set_valor_simulacao(self, new_valor_simulacao):
        self._valor_simulacao = new_valor_simulacao   

    #encapsulamento data_ini_simulacao
    def get_data_ini_simulacao(self):
        return self._data_ini_simulacao
    def set_data_ini_simulacao(self, new_data_ini_simulacao):
        self._data_ini_simulacao = new_data_ini_simulacao   

    #encapsulamento data_fin_simulacao
    def get_data_fin_simulacao(self):
        return self._data_fin_simulacao
    def set_data_fin_simulacao(self, new_data_fin_simulacao):
        self._data_fin_simulacao = new_data_fin_simulacao   

    #encapsulamento retorno_simulacao
    def get_retorno_simulacao(self):
        return self._retorno_simulacao
    def set_retorno_simulacao(self, new_retorno_simulacao):
        self._retorno_simulacao = new_retorno_simulacao   

    #encapsulamento acao_simulacao
    def get_acao_simulacao(self):
        return self._acao_simulacao
    def set_acao_simulacao(self, new_acao_simulacao):
        self._acao_simulacao = new_acao_simulacao    

    #encapsulamento _id_usuario
    def get__id_usuario(self):
        return self._id_usuario

