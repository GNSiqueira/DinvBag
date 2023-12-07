from psycopg2 import Error
from app.config.conexao import Conexao

#metodo de cadastro de usuario
def create_usuario(inform):
    #estabelece a variavel "conn" como a classe que faz a conexão com o banco de dados
    conexao = Conexao()
    conn = conexao.connect()
    #executa os comandos no banco e mostra o resultado
    try:
        cursor = conn.cursor()
        query = "INSERT INTO usuario (nome_usuario, email_usuario, senha_usuario, progresso_usuario) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, inform)
        conn.commit()
        
        return ('Cadastro feito com sucesso!')
    #se caso der errado a insersão dos dados ao banco de dados, mostrara o erro
    except (Exception, Error) as error:
        conn.rollback()
        return("Erro ao inserir dados:", error)
    #finaliza a conexão com o banco de dados
    finally:
        cursor.close()
        conexao.close_connection(conn)

#metodo para checar se o usuario(login) já existe
def verificar_usuario_email(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        cursor.execute("select email_usuario from usuario where email_usuario = '{}'".format(inform))
        results = cursor.fetchall()

        return results[0][0]
    
    except(Exception, Error) as error:
        conn.rollback()
        return False
    finally:
        cursor.close()
        conexao.close_connection(conn)
    
#metodo para checar se o usuario(nome) já existe
def verificar_usuario_nome(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT nome_usuario FROM usuario WHERE nome_usuario = '{}'".format(inform))
        result = cursor.fetchall()

        return result[0][0]
    
    except (Exception, Error) as error:
        conn.rollback()

        return False
    
    finally:
        cursor.close()
        conexao.close_connection(conn)

#metodo para checar se o usuario(senha) já existe
def verificar_usuario_senha(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        cursor.execute("select senha_usuario from usuario where email_usuario = '{}'".format(inform))
        result = cursor.fetchall()

        return result[0][0]
        
    except(Exception, Error) as error:
        conn.rollback()
        return False
    finally:
        cursor.close()
        conexao.close_connection(conn)

#metodo de listagem de usuarios
def read_usuario():
    #estabelece a variavel "conn" como a classe que faz a conexão com o banco de dados
    conexao = Conexao()
    conn = conexao.connect()
    #executa o metodo de select no banco de dados e retorna os usuarios cadastrados
    try:
        cursor = conn.cursor()
        sql = "select * from usuario"
        cursor.execute(sql)
        results = cursor.fetchall()
        usuarios = []
        for result in results:
            usuario = (result[0], result[1], result[2], result[3], result[4])
            usuarios.append(usuario)
        return usuarios
    #caso de errado ou a conexão com o banco ou até a execução do select mostrara o erro 
    except(Exception, Error) as error:
        conn.rollback()
        return("Erro ao listar Usuarios", error)
    #finaliza a conexão com o banco de dados
    finally:
        cursor.close()
        conexao.close_connection(conn)

#metodo para muda a progresso do usuario
def update_progresso_usuario(inform, id):
    #estabelece a variavel conexão como a classe de conexão com o banco de dados
    conexao = Conexao()
    conn = conexao.connect()
    try:
        # executa os comandos no banco de dados
        cursor = conn.cursor()
        cursor.execute("update usuario set progresso_usuario = '{}' where id_usuario = {} ".format(inform, id))
        conn.commit()

        return('Progresso alterada com sucesso!')
    except(Exception, Error) as error:
        # caso de errado mostrara e erro ao usuario
        conn.rollback()
        return('Erro ao atualizar progresso', error)
    finally:
        #fecha a conexão com o banco de dados
        cursor.close()
        conexao.close_connection(conn)

#metodo para muda a nome do usuario
def update_nome_usuario(inform, id):
    #estabelece a variavel conexão como a classe de conexão com o banco de dados
    conexao = Conexao()
    conn = conexao.connect()
    try:
        # executa os comandos no banco de dados
        cursor = conn.cursor()
        cursor.execute("update usuario set nome_usuario = '{}' where id_usuario = {}".format(inform, id))
        conn.commit()

        return('Nome alterada com sucesso!')
    except(Exception, Error) as error:
        # caso de errado mostrara e erro ao usuario
        conn.rollback()
        return('Erro ao atualizar nome', error)
    finally:
        #fecha a conexão com o banco de dados
        cursor.close()
        conexao.close_connection(conn)

#metodo para muda a senha do usuario
def update_senha_usuario(inform, id):
    #estabelece a variavel conexão como a classe de conexão com o banco de dados
    conexao = Conexao()
    conn = conexao.connect()
    try:
        # executa os comandos no banco de dados
        cursor = conn.cursor()
        cursor.execute("update usuario set senha_usuario = '{}' where id_usuario = {} ".format(inform, id))
        conn.commit()

        return('Senha alterada com sucesso!')
    except(Exception, Error) as error:
        # caso de errado mostrara e erro ao usuario
        conn.rollback()
        return('Erro ao atualizar senha', error)
    finally:
        #fecha a conexão com o banco de dados
        cursor.close()
        conexao.close_connection(conn)

#metodo para muda a email do usuario
def update_login_usuario(inform, id):
    #estabelece a variavel conexão como a classe de conexão com o banco de dados
    conexao = Conexao()
    conn = conexao.connect()
    try:
        # executa os comandos no banco de dados
        cursor = conn.cursor()
        cursor.execute("UPDATE usuario SET email_usuario = '{}' WHERE id_usuario = {}".format(inform, id))
        conn.commit()

        return('Login alterado com sucesso!')
    except(Exception, Error) as error:
        # caso de errado mostrara e erro ao usuario
        conn.rollback()
        return('Erro ao atualizar login', error)
    finally:
        #fecha a conexão com o banco de dados
        cursor.close()
        conexao.close_connection(conn)

#metodo deletar usuario
def delete_usuario(inform):
    #estabelece a conexão com o banco
    conexao = Conexao()
    conn = conexao.connect()
    try:
        #executa as linhas de codigo no banco de dados
        cursor = conn.cursor()
        cursor.execute("delete from usuario where id_usuario = {}".format(inform))
        conn.commit()
        return('Usuario deletado com sucesso!')
    except(Exception, Error) as error:
        conn.rollback()
        return('Erro ao deletar usuario', error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

#metodo para obter o id do usuario
def obter_id(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        cursor.execute("select id_usuario from usuario where email_usuario = '{}'".format(inform))
        result = cursor.fetchall()

        return result[0][0]

    except (Exception, Error) as error:
        conn.rollback()
        return('Erro ao obter id do usuario', error)        
    
    finally:
        cursor.close()
        conexao.close_connection(conn)

def pesquisar_usuario(email):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("select  * from usuario where email_usuario = '{}'".format(email))
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    except(Exception, Error) as error:
        return ("Erro ao buscar usuario: ", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_usuario(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update usuario set usuario nome_usuario = %s, email_usuario = %s, senha_usuario = %s where id_usuario = %s;")
        cursor.execute(query, inform)
        conn.commit()
        pass
    except(Exception, Error) as error:
        return ('Erro ao fazer alterações: ', error)
    finally:
        cursor.close()
        conexao.close_connection(conn)