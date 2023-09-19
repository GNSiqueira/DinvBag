from app.models.tipoperguntaModel import TipoPergunta
from app.dao import perguntaDAO, tipoPerguntaDAO
from flask import render_template, request

def carregar_tipo():
    tipoperguntas = []
    results = tipoPerguntaDAO.read_tipo_pergunta()
    for result in results:
        tipopergunta = TipoPergunta(result[0], result[1], result[2])
        tipoperguntas.append(tipopergunta)
    return  tipoperguntas 

def cadastrar_pergunta():
    textopergunta = request.form['textopergunta']
    alt1 = request.form['alt1']
    alt2 = request.form['alt2']
    alt3 = request.form['alt3']
    alt4 = request.form['alt4']
    resposta = request.form['resposta']
    idtipopergunta = request.form['idtipopergunta']
    idquestionario = 1

    resposta = perguntaDAO.create_pergunta(textopergunta, alt1, alt2, alt3, alt4, resposta, idtipopergunta, idquestionario)

    return resposta