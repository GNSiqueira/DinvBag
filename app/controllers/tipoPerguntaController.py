from app.models.tipoperguntaModel import TipoPergunta
from app.dao import tipoPerguntaDAO  

def read_tipo_pergunta():
    tipo_perguntas = []
    results = tipoPerguntaDAO.read_tipo_pergunta()
    for result in results:
        tipopergunta = TipoPergunta(result[0], result[1])
        tipo_perguntas.append(tipopergunta)
    return  tipo_perguntas 

