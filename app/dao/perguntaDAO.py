from psycopg2 import Error 
from app.config.conexao import Conexao
from app.models import perguntaModel

#cria um metodo de cadastro questionario
def create_pergunta(textopergunta, alt1, alt2, alt3, alt4, resposta, idtipopergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("insert into pergunta (texto_pergunta, alternativa1, alternativa2, alternativa3, alternativa4, resposta_pergunta, id_tipo_pergunta) values ('{}','{}','{}','{}','{}','{}',{});".format(textopergunta, alt1, alt2, alt3, alt4, resposta, idtipopergunta))
        cursor.execute(query)
        conn.commit()

        return('Cadastro feito com sucesso!')
    except(Exception, Error) as error:
        conn.rollback()
        return('Erro ao inserir dados:', error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def read_pergunta():
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "select * from pergunta;"
        cursor.execute(query)
        results = cursor.fetchall()
        perguntas = []
        for result in results:
            pergunta = (result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
            perguntas.append(pergunta)
        return perguntas
    except(Exception, Error) as error:
        return('Erro ao carregar pergunta: ', error)
    finally: 
        cursor.close()
        conexao.close_connection(conn)
   
def update_pergunta_textopergunta(idpergunta, textopergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update pergunta set texto_pergunta = '{}' where id_pergunta = {}".format(textopergunta, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Atualização feita com sucesso!"
    except(Exception, Error) as error:
        return ("Atualização não executada:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_pergunta_alternativa1(idpergunta, alternativa1):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update pergunta set alternativa1 = '{}' where id_pergunta = {}".format(alternativa1, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Atualização feita com sucesso!"
    except(Exception, Error) as error:
        return ("Atualização não executada:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_pergunta_alternativa2(idpergunta, alternativa2):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update pergunta set alternativa2 = '{}' where id_pergunta = {}".format(alternativa2, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Atualização feita com sucesso!"
    except(Exception, Error) as error:
        return ("Atualização não executada:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_pergunta_alternativa3(idpergunta, alternativa3):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update pergunta set alternativa3 = '{}' where id_pergunta = {}".format(alternativa3, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Atualização feita com sucesso!"
    except(Exception, Error) as error:
        return ("Atualização não executada:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_pergunta_alternativa4(idpergunta, alternativa4):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update pergunta set alternativa4 = '{}' where id_pergunta = {}".format(alternativa4, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Atualização feita com sucesso!"
    except(Exception, Error) as error:
        return ("Atualização não executada:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_pergunta_resposta(idpergunta, resposta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update pergunta set resposta_pergunta = '{}' where id_pergunta = {}".format(resposta, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Atualização feita com sucesso!"
    except(Exception, Error) as error:
        return ("Atualização não executada:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_pergunta_id_tipo(idpergunta, id_tipo):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("update pergunta set id_tipo_pergunta = '{}' where id_pergunta = {}".format(id_tipo, idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Atualização feita com sucesso!"
    except(Exception, Error) as error:
        return ("Atualização não executada:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def delete_pergunta(idpergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("delete from pergunta where id_pergunta = {}".format(idpergunta))
        cursor.execute(query)
        conn.commit()
        return "Pergunta deletada com sucesso!"
    except(Exception, Error) as error:
        return ("Erro ao deletar pergunta: ", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)
        
    