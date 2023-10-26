from app.models.tipoperguntaModel import TipoPergunta
from app.dao import tipoPerguntaDAO  

def read_tipo_pergunta():
    tipoperguntas = []
    results = tipoPerguntaDAO.read_tipo_pergunta()
    for result in results:
        tipopergunta = TipoPergunta(result[0], result[1], result[2])
        tipoperguntas.append(tipopergunta)
    return  tipoperguntas 

