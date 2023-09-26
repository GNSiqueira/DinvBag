from psycopg2 import connect, Error

class Conexao:
    def connect(self):
        try:
            conn = connect(
                host="localhost",
                port="5432",
                database="DinvBag",
                user="postgres",
                password="123456"
            )
            return conn
        except (Exception, Error) as error:
            return("Erro ao conectar no banco:", error)

    def close_connection(self, conn):
        try:
            if conn is not None:
                conn.close()
                return("Conexão fechada com sucesso!")
        except (Exception, Error) as error:
            return("Erro ao fechar conexão:", error)


