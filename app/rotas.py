from flask import Flask, render_template, request
from app import app
from app.controllers import usuarioController, perguntaController

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

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    resposta = usuarioController.cadastra()
    return render_template('cadastro.html', static = 'app/static', resposta = resposta)

@app.route('/logar', methods=['POST'])
def logar():
    resposta = usuarioController.loga()
    return render_template('loginprincipal.html', static = 'app/static', resposta = resposta)
@app.route('/tesouro')
def tesouro():
    return render_template('tesouro.html', static = 'app/static')
@app.route('/questionariotesouro')
def questionariotesouro():
    return render_template('questionariotesouro.html', static = 'app/static')

@app.route('/conf_user')
def conf_user():
    return render_template('editarUsuario.html')

@app.route('/delet')
def delet():
    return render_template('deletar.html')

@app.route('/confirma', methods=['POST'])
def confirma():
    
    if  usuarioController.confirma_form() == True:
        return render_template('editar.html')
    else:
        resposta = usuarioController.confirma_form()
        return render_template('editarUsuario.html', resposta = resposta)

@app.route('/editar_login', methods=['POST'])
def update_login():
    resposta = usuarioController.update_login_form()
    return render_template('editar.html', resposta_login = resposta)
    
@app.route('/editar_senha', methods=['POST'])
def update_senha():
    resposta = usuarioController.update_senha_form()
    return render_template('editar.html', resposta_senha = resposta)

@app.route('/editar_nome', methods=['POST'])
def update_nome():
    resposta = usuarioController.update_nome_form()
    return render_template('editar.html', resposta_nome = resposta)

@app.route('/deletar', methods=['POST'])
def deletar():
    resposta = usuarioController.delet_form()
    return render_template('deletar.html', resposta = resposta)

@app.route('/cadastrarP', methods=['GET'])
def cadastrar_pergunta_entrar():
    tipoperguntas = perguntaController.carregar_tipo()
    return render_template('cadastrarpergunta.html', tipoperguntas = tipoperguntas)

@app.route("/cadastrar_pergunta_enviar", methods={'POST'})
def cadastrar_pergunta():
    resposta = perguntaController.cadastrar_pergunta()
    return render_template('cadastrarpergunta.html', resposta = resposta)