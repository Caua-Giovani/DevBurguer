from flask import Flask, jsonify, render_template,request,redirect,session,flash
import mysql
import mysql.connector

from model.lanches import recuperar_lanches
from model.lanches import recuperar_lanches_unit
from model.lanches import recuperar_lanches_destaque
from model.lanches import recuperar_lanches_carrinho
from model.lanches import adicionar_lanche_carrinho

from model.usuario import adicionar_usuario
from model.usuario import autenticar_usuario


app = Flask(__name__)

app.secret_key='chave-secreta-demais'

@app.route("/")
def pag_principal():
    return render_template("home.html")

@app.route("/unit/<int:id>")
def pag_unitario(id):
    lanches = recuperar_lanches_unit(id)
    return render_template("pagina2.html",lanches=lanches)

@app.route("/cardapio")
def pag_cardapio():
    lanches = recuperar_lanches()
    destaque = recuperar_lanches_destaque()
    if 'usuario_logado' in session:
        return render_template("index.html",lanches=lanches,destaque=destaque)
    else:
        return redirect("/login")



@app.route("/carrinho")
def pag_carrinho():
    return jsonify(recuperar_lanches_carrinho(session['usuario_logado'])),200

@app.route("/carrinho/post/<int:id>")
def pag_carrinho_post(id):
    adicionar_lanche_carrinho(id,session['usuario_logado'])
    return redirect("/cardapio")


    
@app.route("/login")
def pag_login():
    return render_template("login.html")

@app.route("/cadastro")
def pag_cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro/post",methods=["POST"])
def pag_cadastro_post():
    login = request.form.get("login_create")
    senha = request.form.get("senha_create")
    nome = request.form.get("nome_create")
    adicionar_usuario(login,senha,nome)

    return redirect("/login")


@app.route("/login/post",methods=["POST"])
def pag_login_post():

    login= request.form.get("login")
    senha= request.form.get("senha")

    if autenticar_usuario(login,senha):
        session['usuario_logado'] = login
        return redirect("/cardapio")
    else:
        flash("Usuário ou senha incorretos!")
        return redirect("/login")
    

@app.route("/contato")
def pag_contato():
    return render_template("contato.html")


@app.route("/logout")
def clear_session():
    session.clear()
    return redirect("/login")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)

