from psycopg2 import Error
from app.config.conexao import Conexao

#create resposta
def create_resposta(alternativa_respondida, alternativa_correta, datapergunta, idquestionario, idperguta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("insert into resposta (alternativa_respondida, alternativa_correta, data_pergunta, id_questionario, id_pergunta) values ({}, {}, {}, {}, {})".format(alternativa_respondida, alternativa_correta, datapergunta, idquestionario, idperguta))
        cursor.execute(query)
        conn.commit()
        return "Resposta adicionada com sucesso!"
    
    except(Exception, Error) as error:
        return("Erro ao inserir dados:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(alternativa_respondida)
def update_resposta_alternativa_respondida(id, alternativa_respondida):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set alternativa_respondida = {} where id_resposta = {}".format(id, alternativa_respondida))
        cursor.execute(query)
        conn.commit()
        return "Alternativa respondida alterada com sucesso!"
    except(Exception, Error) as error:
        return("Erro ao atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(alternativa_correta)
def update_resposta_alternativa_correta(id, alternativa_correta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set alternativa_correta = {} where id_resposta = {}".format(id, alternativa_correta))
        cursor.execute(query)
        conn.commit()
        return "Alternativa correta atualizada com sucesso!"

    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(data_resposta)
def update_resposta_data_resposta(id, data_resposta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set data_resposta = {} where id_resposta = {}".format(id, data_resposta))
        cursor.execute(query)
        conn.commit()
        return "Data da resposta atualizada com sucesso!"

    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(id_questionario)
def update_resposta_id_questionario(id, id_questionario):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set id_questionario = {} where id_resposta = {}".format(id, id_questionario))
        cursor.execute(query)
        conn.commit()
        return "IdQuestionario atualizado com sucesso!"

    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(id_pergunta)
def update_resposta_id_pergunta(id, idpergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set id_pergunta = {} where id_resposta = {}".format(id, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "IdPergunta atualizada com sucesso!"

    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#read resposta
def read_resposta():
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "select * form resposta"
        cursor.execute(query)
        results = cursor.fetchall()
        respostas = []
        for result in results:
            resposta = (result[0], result[1], result[2], result[3], result[4], result[5])
            respostas.append(resposta)
        return respostas
    except(Exception, Error) as error:
        return("Erro ao listar respostas:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#delet resposta
def delet_resposta(id):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("delete from resposta where id_resposta = {}".format(id))
        cursor.execute(query)
        conn.commit()
        return "Resposta deletada com sucesso!"
    
    except(Exception, Error) as error:
        return ("Erro ao deletar resposta", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()
    