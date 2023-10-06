from app.models.usuarioModel import Usuario
from app.dao import usuarioDAO
from flask import request, render_template
from app.rotas import app

#metodo de cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    if usuarioDAO.verificar_usuario_email(email) == email:
        resposta = 'Email já cadastrado!'
        return resposta
    else:
        if usuarioDAO.verificar_usuario_nome(nome) == nome:
            resposta = 'Nome já cadastrado! Tente outro!'
            return resposta
        else:
            user = Usuario(1, nome, email, senha, 'Inicio')
            inform = [user.get_nome_usuario(), user.get_email_usuario(), user.get_senha_usuario(), user.get_progresso_usuario()]
            resposta = usuarioDAO.create_usuario(inform)
            return resposta
        
#method de login          
def login():
    login = None
    senha = None
    login = request.form['email']
    senha = request.form['senha']
    if usuarioDAO.verificar_usuario_email(login) == login:
        if usuarioDAO.verificar_usuario_senha(login) == senha:
            return 'Usuario entra'
        else:
            return  'Usuario ou senha invalida'
    else:
        return  'Usuario ou senha invalida'
    
#metodo de listar
@app.route('/listar', methods=['GET'])
def read_usuario():
    usuarios = []
    results = usuarioDAO.read_usuario()
    for result in results:
        usuario = Usuario(result[0], result[1], result[2], result[3], result[4])
        usuarios.append(usuario)
    return render_template('listar.html', usuarios=usuarios)

#metodo de pegar codigo do usuario
@app.route('/pegar_id', methods=['GET'])
def __init__():
    usuarios = []
    results = usuarioDAO.read_usuario()
    for result in results:
        usuario = Usuario(result[0], result[1], result[2], result[3], result[4])
        usuarios.append(usuario)
    return render_template('pegarid.html', usuarios = usuarios)

#precessar o id
@app.route('/processar', methods=['POST'])
def processar():
    usuarios = []
    results = usuarioDAO.read_usuario()
    for result in results:
        usuario = Usuario(result[0], result[1], result[2], result[3], result[4])
        usuarios.append(usuario)
    id_selecionado = request.form['id_usuario']
    # Faça algo com o ID selecionado, como armazená-lo em uma variável ou processá-lo
    return render_template('pegarid.html', id_selecionado = id_selecionado, usuarios = usuarios)

@app.route('/confirma', methods=['GET'])
def confirma_form():
    login = None
    nome = None
    senha = None
    login = request.form['login']
    nome = request.form['nome']
    senha = request.form['senha']
    if usuarioDAO.verificar_usuario_email(login) == login:
        if usuarioDAO.verificar_usuario_nome(login) == nome:
            if usuarioDAO.verificar_usuario_senha(login) == senha:
                global id_sisten
                global login_sisten
                id_sisten = int(usuarioDAO.obter_id(login))
                login_sisten = login
                return True
                
            else:
                resposta = 'Senha Incorreta'
                return resposta 
        
        else:
            resposta = 'Nome Incorreta'
            return resposta 
    
    else:
        resposta = 'Email não existente'
        return resposta 
    
@app.route('/editar_login', methods=['GET'])
def update_login_form():
    global id_sisten
    if id_sisten != None:
        login = request.form['login_up']
        resposta = usuarioDAO.update_login_usuario(login, id_sisten)
        id_sisten = None
        return resposta
    else:
        return 'Confirmar usuario novamente, volte a pagina anterior!'

@app.route('/editar_senha', methods=['GET'])
def update_senha_form():
    global id_sisten
    if id_sisten != None:
        senha = request.form['senha']
        resposta = usuarioDAO.update_senha_usuario(senha, id_sisten)
        id_sisten = None
        return resposta
    else:
        return 'Confirmar usuario novamente, volte a pagina anterior!'

@app.route('/editar_nome', methods=['GET'])
def update_nome_form():
    global id_sisten
    if id_sisten != None:
        nome = request.form['nome']
        resposta = usuarioDAO.update_nome_usuario(nome, id_sisten)
        id_sisten = None
        return resposta
    else:
        return 'Confirmar usuario novamente, volte a pagina anterior!'
    
@app.route('/deletar', methods=['GET'])
def delet_form():
    nome = request.form['nome_delet']
    senha = request.form['senha_delet']
    login = request.form['login_delet']
    if usuarioDAO.verificar_usuario_email(login) == login:
        if usuarioDAO.verificar_usuario_nome(login) == nome:
            if usuarioDAO.verificar_usuario_senha(login) == senha:
                id_user = usuarioDAO.obter_id(login)
                resposta = usuarioDAO.delete_usuario(id_user)
                return resposta
            else:
                resposta = 'Senha Incorreta'
                return resposta 
        
        else:
            resposta = 'Nome Incorreta'
            return resposta 
    
    else:
        resposta = 'Email não existente'
        return resposta 