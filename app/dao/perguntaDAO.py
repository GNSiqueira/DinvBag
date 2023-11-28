from psycopg2 import Error 
from app.config.conexao import Conexao

#cria um metodo de cadastro questionario
def create_pergunta(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "insert into pergunta (texto_pergunta, alternativa1, alternativa2, alternativa3, alternativa4, resposta_pergunta, id_tipo_pergunta) values (%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(query, inform)
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
        
def contar_perguntas(tipo):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("select count(p.id_pergunta) from pergunta p inner join tipo_pergunta t on t.id_tipo_pergunta = p.id_tipo_pergunta where tipo_pergunta = '{}'".format(tipo))
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]
    except(Exception, Error) as error:
        return('Erro no codigo do banco: ', error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def selecionar_perguntas(tipo):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("select p.* from pergunta p inner join tipo_pergunta t on t.id_tipo_pergunta = p.id_tipo_pergunta where tipo_pergunta = {};".format(tipo))
        cursor.execute(query)
        results = cursor.fetchall()
        conn.commit()
        return results
    except(Exception, Error) as error:
        return('Erro no codigo do banco: ', error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def read_pergunta_um(id):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("select * from pergunta where id_pergunta = {};".format(id))
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

def verificar_pergunta(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("select * from pergunta where texto_pergunta = %s and alternativa1 = %s and alternativa2 = %s and alternativa3 = %s and alternativa4 = %s;")
        cursor.execute(query, inform)
        results = cursor.fetchall()
        perguntas = []
        for result in results:
            pergunta = (result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
            perguntas.append(pergunta)
        return results
    except(Exception, Error) as error:
        return('Erro ao carregar pergunta: ', error)
    finally: 
        cursor.close()
        conexao.close_connection(conn)

def update_pergunta(inform):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "update pergunta set texto_pergunta = %s, alternativa1 = %s, alternativa2 = %s, alternativa3 = %s, alternativa4 = %s, resposta_pergunta = %s, id_tipo_pergunta = %s where id_pergunta = %s;"
        cursor.execute(query, inform)
        conn.commit()

        return ('Uptate feito com sucesso!')
    except(Exception, Error) as error:
        return('Erro ao carregar pergunta: ', error)
    finally: 
        cursor.close()
        conexao.close_connection(conn)
