from flask import Flask, render_template, request
from app import app
from app.controllers import usuarioController

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/singup', methods=['POST'])
def singup():
    resposta = None
    resposta = usuarioController.singup_form()
    return render_template('index.html', resposta = resposta)

@app.route('/logar')
def logar():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    retorno = usuarioController.login_form()
    if retorno == True:
        resposta =  'Usuario Entra'
    
    else:
        resposta = 'Usuario ou senha invalida'

    return render_template('login.html', resposta=resposta)

@app.route('/conf_user')
def conf_user():
    return render_template('editarUsuario.html')

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

@app.route('/delet', methods=['POST'])
def delet():
    return render_template('deletar.html')

@app.route('/deletar', methods=['POST'])
def deletar():
    resposta = usuarioController.delet_form()
    return render_template('deletar.html', resposta = resposta)