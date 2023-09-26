
class Usuario:
    def __init__(self,id_usuario, nome_usuario, email_usuario, senha_usuario, progresso_usuario):
        self._id_usuario = id_usuario
        self._nome_usuario = nome_usuario
        self._email_usuario = email_usuario
        self._senha_usuario = senha_usuario
        self._progresso_usuario = progresso_usuario

    #encapsulamento idusuario
    def get_idusuario(self):
        return self._id_usuario

    # encapsulamento nome_usuario 
    def get_nome_usuario(self):
        return self._nome_usuario
    def set_nome_usuairo(self,new_nome_usuario):
        self._nome_usuario = new_nome_usuario

    # encapsulamento email_usuario
    def get_email_usuario(self):
        return self._email_usuario
    def set_email_usuario(self, new_email_usuario):
        self._email_usuario = new_email_usuario

    # encapsulamento senha_usuario
    def get_senha_usuario(self):
        return self._senha_usuario
    def set_senha_usuario(self, new_senha_usuario):
        self._senha_usuario = new_senha_usuario

    # encapsulamento progresso_usuario
    def get_progresso_usuario(self):
        return self._progresso_usuario
    def set_progresso_usuario(self, new_progresso_usuario):
        self._progresso_usuario = new_progresso_usuario
