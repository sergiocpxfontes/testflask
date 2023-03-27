from flask import Flask, render_template,redirect,request,url_for,jsonify
app= Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html",message="Bem vindo")