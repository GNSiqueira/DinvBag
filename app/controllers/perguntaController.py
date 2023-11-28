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

def read_pergunta():
    results = perguntaDAO.read_pergunta()
    perguntas = []
    for result in results:
        pergunta = Pergunta(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        perguntas.append(pergunta)
        
    return perguntas

def read_pergunta_um():    
    ab = request.args['id-pergunta']
    ass = []
    results = perguntaDAO.read_pergunta_um(ab)
    for result in results:
        a = Pergunta(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        ass.append(a)
    return ass

def cadastrar_pergunta():
    a = request.form['texto-pergunta']
    b = request.form['alternativa1']
    c = request.form['alternativa2']
    d = request.form['alternativa3']
    e = request.form['alternativa4']
    f = request.form['resposta-pergunta']
    g = request.form['id-tipo-pergunta']
    classe = Pergunta(None, a, b, c, d, e, f, g)
    h = perguntaDAO.verificar_pergunta(inform = [classe.get_texto_pergunta(), classe.get_alternativa1(), classe.get_alternativa2(), classe.get_alternativa3(), classe.get_alternativa4()])
    print (h)
    if h == []:
       i =  perguntaDAO.create_pergunta(inform = [classe.get_texto_pergunta(), classe.get_alternativa1(), classe.get_alternativa2(), classe.get_alternativa3(), classe.get_alternativa4(), classe.get_resposta_pergunta(), classe.get_id_tipo_pergunta()])
       print (i)
    
    pass

def editar_pergunta():
    h = request.form['id-pergunta']
    a = request.form['texto-pergunta']
    b = request.form['alternativa1']
    c = request.form['alternativa2']
    d = request.form['alternativa3']
    e = request.form['alternativa4']
    f = request.form['resposta-pergunta']
    g = request.form['id-tipo-pergunta']
    classe = Pergunta(h, a, b, c, d, e, f, g)
    i = perguntaDAO.update_pergunta(inform = [classe.get_texto_pergunta(), classe.get_alternativa1(), classe.get_alternativa2(), classe.get_alternativa3(), classe.get_alternativa4(), classe.get_resposta_pergunta(), classe.get_id_tipo_pergunta(), classe.get_id_pergunta()])
    pass

def deletar_pergunta():
    if request.method == "POST":
        a = request.form['id-pergunta']
        perguntaDAO.delete_pergunta(a)
    pass 