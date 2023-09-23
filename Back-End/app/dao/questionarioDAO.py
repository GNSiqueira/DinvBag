from psycopg2 import Error
from app.config.conexao import Conexao
from app.models import questionarioModel

#cria um metodo de cadastrar questionario
def create_questionario(estagio, acertos):
    #cria conexao com o banco
    conexao = Conexao()
    conn = conexao.connect()
    try: 
        cursor = conn.cursor()
        query = ("insert into questionario (fase_questionario, acertos_questionario) values ('{}', {})".format(estagio, acertos))
        cursor.execute(query)
        conn.commit()

        return ('Cadastro feito com sucesso!')
    except(Exception, Error) as error:
        conn.rollback()
        return("Erro ao inserir dados:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

# listar questionario
def read_questionario():
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "select * from questionario"
        cursor.execute(query)
        results = cursor.fetchall()
        usuarios = []
        for result in results:
            usuario = (result[0], result[1], result[2])
            usuarios.append(usuario)
        return usuarios
    except(Exception, Error) as error:
        return("Erro ao carregar dados:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

#atualizar questionario(estagio)
def update_questionario_estagio(id, estagio):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update questionario set fase_questionario = '{}' where = id_questionario = {}".format(estagio, id))
        cursor.execute(query)
        conn.commit()

        return("Estagio atualizado com sucesso!")
    except(Exception, Error) as error:
        return("Error ao atualizar questionario", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#atualizar questionario(acertos)
def update_questionario_acertos(id, acertos):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update questionario set acertos_questionario = '{}' where id_questionario = {}".format(acertos, id))
        cursor.execute(query)
        conn.commit()

        return("Acertos atualizado com sucesso!")
    except(Exception, Error) as error:
        return("Error ao atualizar questionario", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#deleta questionario
def delet_questionario(id):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("delete from questionario where id_questionario = {}".format(id))
        cursor.execute(query)
        conn.commit()
        
        return "Questionatio deletado!"
    except(Exception, Error) as error:
        return ("Erro ao deletar Questionario:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

