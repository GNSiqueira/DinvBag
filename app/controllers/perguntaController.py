from app.models.perguntaModel import Pergunta
from app.controllers import tipoPerguntaController
from app.dao import perguntaDAO
from flask import request
from random import sample

def carregar_questionario_tesouro():
    retorno = {
        'tipo_questionario': 'TESOURO SELIC'
    }
    
    pergunta = 0
    
    tipo = 'Tesouro Selic'
    contagem = perguntaDAO.contar_perguntas(tipo)
    aleatorio = sample(range(contagem), 5)
    for c in range(0, 5):
        cccc = 2
        resp = perguntaDAO.selecionar_perguntas(tipo)[aleatorio[c]]
        pergunta +=1
        retorno['texto_questionario{}'.format(pergunta)] = resp[1]
        
        for cc in range(1, 6):
            retorno['alter{}_p{}'.format(cc, pergunta)] = resp[cccc]
            cccc+=1
    return retorno