from psycopg2 import Error
from app.config.conexao import Conexao

def create_tipo_pergunta(nometipopergunta, descricaopergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "insert into tipopergunta (nometipopergunta, descricaopergunta) values ({}, {});".format(nometipopergunta, descricaopergunta)
        cursor.execute(query)
        conn.commit()
        return "Cadastro de pergunta feita com sucesso!"
    except(Exception, Error) as error:
        return ("Erro ao fazer cadastro:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def read_tipo_pergunta():
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "select * from tipopergunta;"
        cursor.execute(query)
        results = cursor.fetchall()
        tipo_perguntas = []
        for result in results:
            tipo_pergunta = (result[0], result[1], result[2])
            tipo_perguntas.append(tipo_pergunta)
        return tipo_perguntas
    except (Exception, Error) as error:
        return ("Erro ao listar Tipo Perguntas:", error)
    finally:
        cursor.close()
        conexao.close_connection(conn)

def update_tipo_pergunta_nometipopergunta(nometipopergunta, idtipopergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "update tipopergunta set nometipopergunta = '{}' where idtipopergunta = '{}';".format(nometipopergunta, idtipopergunta)

    except (Exception, Error) as error:
        return ("Erro ao alterar tipo de pergunta: " , error)
    finally: 
        cursor.close()
        conexao.close_connection(conn)

def update_tipo_pergunta_descricaopergunta(descricaopergunta, idtipopergunta):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = "update tipopergunta set descricaopergunta = '{}' where idtipopergunta = '{}';".format(descricaopergunta, idtipopergunta)

    except (Exception, Error) as error:
        return ("Erro ao alterar descricao tipo pergunta: " , error)
    finally: 
        cursor.close()
        conexao.close_connection(conn)

