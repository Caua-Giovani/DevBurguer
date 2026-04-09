from flask import Flask, render_template,request,redirect,session,flash
import mysql
import mysql.connector

from model.lanches import recuperar_lanches

app = Flask(__name__)

app.secret_key='chave-secreta-demais'

@app.route("/")
def pag_principal():
    return render_template("layout.html")

@app.route("/unit")
def pag_unitario():
    lanches = recuperar_lanches()
    return render_template("pagina2.html",lanches=lanches)

@app.route("/cardapio")
def pag_cardapio():
    lanches = recuperar_lanches()
    return render_template("index.html",lanches=lanches)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)

