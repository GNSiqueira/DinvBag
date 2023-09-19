from psycopg2 import Error 
from app.config.conexao import Conexao

#cria um metodo de cadastro questionario
def create_pergunta(textopergunta, alt1, alt2, alt3, alt4, resposta, idpergunta, idquestionario):
    conexao = Conexao()
    conn = conexao.connect()
    try:
        cursor = conn.cursor()
        query = ("insert into pergunta (textopergunta, alt1, alt2, alt3, alt4, resposta, idtipopergunta, idquestionario) values ('{}','{}','{}','{}','{}','{}',{},{});".format(textopergunta, alt1, alt2, alt3, alt4, resposta, idpergunta, idquestionario))
        cursor.execute(query)
        conn.commit()

        return('Cadastro feito com sucesso!')
    except(Exception, Error) as error:
        conn.rollback()
        return('Erro ao inserir dados:', error)
    finally:
        cursor.close()
        conexao.close_connection(conn)
