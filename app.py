from flask import Flask, render_template,request,redirect,session,flash
import mysql
import mysql.connector

from model.lanches import recuperar_lanches
from model.lanches import recuperar_lanches_unit
from model.lanches import recuperar_lanches_destaque

app = Flask(__name__)

app.secret_key='chave-secreta-demais'

@app.route("/")
def pag_principal():
    return render_template("layout.html")

@app.route("/unit/<int:id>")
def pag_unitario(id):
    lanches = recuperar_lanches_unit(id)
    return render_template("pagina2.html",lanches=lanches)

@app.route("/cardapio")
def pag_cardapio():
    lanches = recuperar_lanches()
    destaque = recuperar_lanches_destaque()
    return render_template("index.html",lanches=lanches,destaque=destaque)




if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)

