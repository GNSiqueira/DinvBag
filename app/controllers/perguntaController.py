from app.models.perguntaModel import Pergunta
from app.models.tipoperguntaModel import TipoPergunta
from app.dao import perguntaDAO, tipoPerguntaDAO
from flask import request, render_template
from app.controllers.rotas import app

@app.route('/cadastrar_pergunta', methods=['GET'])
def __init__():
    idtipoperguntas = []
    results = perguntaDAO.read_()
    for result in results:
        idtipopergunta = TipoPergunta(result[0], result[1], result[2])
        idtipoperguntas.append(idtipopergunta)
    return render_template('cadastrarPergunta.html', tipoperguntas = idtipoperguntas)