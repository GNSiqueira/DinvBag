from app.models.usuarioModel import Usuario
from app.dao import usuarioDAO
from flask import request, render_template, make_response

def para_string(var):
    return str(var)

def para_int(var):
    return int(var)

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
            cookies = make_response(render_template('cadastro.html', static = 'app/static', resposta = resposta))
            id_user = usuarioDAO.pesquisar_usuario(email)
            cookies.set_cookie("iduser", para_string(id_user))
            return resposta
        
#método de login      
def loga():
    login = request.form['login']
    senha = request.form['senha']
    login_1 = usuarioDAO.verificar_usuario_email(login)
    senha_1 = usuarioDAO.verificar_usuario_senha(login) 
    if login_1 == login:
        if senha_1 == senha:
            resposta = 'Usuario entra!'
            cookies = make_response(render_template('loginprincipal.html', static = 'app/static', resposta = resposta))
            id_user = usuarioDAO.pesquisar_usuario(login)
            cookies.set_cookie("iduser", para_string(id_user))
            return cookies
        
        else:
            resposta = 'Usuario ou senha invalida'
            return resposta
    else:
        resposta = 'Usuario ou senha invalida'
        return  resposta