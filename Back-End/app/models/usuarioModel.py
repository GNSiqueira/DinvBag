
class Usuario:
    def __init__(self,idusuario, nomeusuario, login, senha, progresso):
        self._idusuario = idusuario
        self._nomeusuario = nomeusuario
        self._login = login
        self._senha = senha
        self._progresso = progresso

    #encapsulamento idusuario
    def get_idusuario(self):
        return self._idusuario

    # encapsulamento nomeusuario 
    def get_nomeusuario(self):
        return self._nomeusuario
    def set_nomeusuairo(self,new_nomeusuario):
        self._nomeusuario = new_nomeusuario

    # encapsulamento login
    def get_login(self):
        return self._login
    def set_login(self, new_login):
        self._login = new_login

    # encapsulamento senha
    def get_senha(self):
        return self._senha
    def set_senha(self, new_senha):
        self._senha = new_senha

    # encapsulamento progresso
    def get_progresso(self):
        return self._progresso
    def set_progresso(self, new_progresso):
        self._progresso = new_progresso
