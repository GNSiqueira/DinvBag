from psycopg2 import Error
from app.config.conexao import Conexao

#create resposta
def create_resposta(descricaoresposta, alternativaescolhida, datapergunta, idusuario, idperguta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("insert into resposta (descricaoresposta, alternativaescolhida, datapergunta, idusuario, idperguta) values ({}, {}, {}, {}, {})".format(descricaoresposta, alternativaescolhida, datapergunta, idusuario, idperguta))
        cursor.execute(query)
        conn.commit()
        return "Resposta adicionada com sucesso!"
    
    except(Exception, Error) as error:
        return("Erro ao inserir dados:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(descricaoresposta)
def update_resposta_descricao(id, descricao):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set descricaoresposta = {} where idresposta = {}".format(id, descricao))
        cursor.execute(query)
        conn.commit()
        return "Descrição alterada com sucesso!"
    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(alternativaescolhida)
def update_resposta_alternativa(id, alternativa):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set alternativaescolhida = {} where idresposta = {}".format(id, alternativa))
        cursor.execute(query)
        conn.commit()
        return "Alternativa escolhica atualizada com sucesso!"

    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(datapergunta)
def update_resposta_descricao(id, data):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set dataresposta = {} where idresposta = {}".format(id, data))
        cursor.execute(query)
        conn.commit()
        return "Data da pergunta atualizada com sucesso!"

    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(idusuario)
def update_resposta_idusuario(id, idusuario):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set idusuario = {} where idresposta = {}".format(id, idusuario))
        cursor.execute(query)
        conn.commit()
        return "IdUsuario atualizado com sucesso!"

    except(Exception, Error) as error:
        return("Erro au atualizar informação:", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()

#update resposta(idpergunta)
def update_resposta_idpergunta(id, idpergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update resposta set idpergunta = {} where idresposta = {}".format(id, idpergunta))
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
        query = ("delete from resposta where idresposta = {}".format(id))
        cursor.execute(query)
        conn.commit()
        return "Resposta deletada com sucesso!"
    
    except(Exception, Error) as error:
        return ("Erro ao deletar resposta", error)
    finally:
        conexao.close_connection(conn)
        cursor.close()
    