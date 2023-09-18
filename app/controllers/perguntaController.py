from app.models.tipoperguntaModel import TipoPergunta
from app.dao import perguntaDAO, tipoPerguntaDAO
from flask import render_template

def carregar_tipo():
    tipoperguntas = []
    results = tipoPerguntaDAO.read_tipo_pergunta()
    for result in results:
        tipopergunta = TipoPergunta(result[0], result[1], result[2])
        tipoperguntas.append(tipopergunta)
    return  tipoperguntas 
