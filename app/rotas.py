from flask import Flask, render_template, request, redirect, url_for
from app import app
from app.controllers import usuarioController, perguntaController, questionarioController, tipoPerguntaController

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html", static = 'app/static/')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', static = 'app/static')

@app.route('/login')
def login():
    return render_template('loginprincipal.html', static = 'app/static')


@app.route('/tesouro')
def tesouro():
    return render_template('tesouro.html', static = 'app/static')

@app.route('/acoes')
def acoes():
    return render_template('acoes.html', static = 'app/static')

@app.route('/cbd')
def cbd():
    return render_template('cbd.html', static = 'app/static')

@app.route('/elements')
def elements():
    return render_template('elements.html', static = 'app/static')

@app.route('/fundo')
def fundo():
    return render_template('fundo.html', static = 'app/static')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    resposta = usuarioController.cadastra()
    return resposta

@app.route('/logar', methods=['POST'])
def logar():
    resposta = usuarioController.loga()
    return resposta

@app.route('/questionario')
def questionariotesouro():
    retorno = perguntaController.carregar_questionario_tesouro()
    questionarioController.criar_questionario()
    return render_template('questionario.html', static = 'app/static', dados = retorno)

@app.route('/pergunta', methods=['POST', 'GET'])
def cadastrar_pergunta():
    if request.method == "POST":
        perguntaController.cadastrar_pergunta()             
        return redirect(url_for('cadastrar_pergunta'))
    else:
        tipo_pergunta = tipoPerguntaController.read_tipo_pergunta()
        todas_perguntas = perguntaController.read_pergunta()        
        return render_template('pergunta.html',  tipo_perguntas = tipo_pergunta, carregadas = todas_perguntas)

@app.route('/pergunta/editar', methods=['POST', 'GET'])
def editar_pergunta():
    if request.method == 'POST':
        perguntaController.editar_pergunta()
        return redirect(url_for('cadastrar_pergunta'))

    else: 
        tipo_pergunta = tipoPerguntaController.read_tipo_pergunta()
        carregadas = perguntaController.read_pergunta_um() 
        return render_template('editarpergunta.html', carregadas = carregadas, tipo_perguntas = tipo_pergunta)

@app.route('/pergunta/deletar', methods=['POST'])
def deletar_pergunta():
    perguntaController.deletar_pergunta()
    return redirect(url_for('cadastrar_pergunta'))

@app.route('/perfil', methods=['GET', 'POST'])
def perfil():
    return render_template('perfil.html', static = 'app/static')

@app.route('/ver')
def cookies():
    return request.cookies
    