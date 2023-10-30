from app.models.usuarioModel import Usuario
from app.dao import usuarioDAO
from flask import request, render_template, make_response

#metodo de cadastro
def cadastra():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    email_1 = usuarioDAO.verificar_usuario_email(email) 
    nome_1 = usuarioDAO.verificar_usuario_nome(nome)
    if email_1 == email:
        resposta = 'Email já cadastrado!'
        return resposta
    else:
        if nome_1 == nome:
            resposta = 'Nome já cadastrado! Tente outro!'
            return resposta
        else:
            user = Usuario(1, nome, email, senha, 'Inicio')
            inform = [user.get_nome_usuario(), user.get_email_usuario(), user.get_senha_usuario(), user.get_progresso_usuario()]
            resposta = usuarioDAO.create_usuario(inform)
            id_usuario = usuarioDAO.pesquisar_usuario(email)
            cookies = make_response()
            cookies.set_cookie('id_usuario', id_usuario)
            return resposta
        
#método de login      
def loga():
    login = request.form['login']
    senha = request.form['senha']
    login_1 = usuarioDAO.verificar_usuario_email(login)
    senha_1 = usuarioDAO.verificar_usuario_senha(login) 
    if login_1 == login:
        if senha_1 == senha:
            resposta = 'Usuario entra'
            id_usuario = usuarioDAO.pesquisar_usuario(login)
            cookies = make_response()
            cookies.set_cookie('id_usuario', id_usuario)
            return resposta
        else:
            resposta = 'Usuario ou senha invalida'
            return resposta
    else:
        resposta = 'Usuario ou senha invalida'
        return  resposta