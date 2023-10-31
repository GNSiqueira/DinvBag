from app.models.questionarioModel import Questionario
from app.dao import questionarioDAO
from flask import request

def para_string(var):
    return str(var)

def para_int(var):
    return int(var)

def criar_questionario():
    estagio = 'Primeiro'
    acertos = 0
    cookies = request.cookies
    id_user = para_int(cookies["iduser"])
    verificar = questionarioDAO.pesquisar_questionario(id_user, estagio)
    if verificar != estagio:
        result = questionarioDAO.create_questionario(estagio, acertos, id_user)
    pass 