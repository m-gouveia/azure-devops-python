from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hola FIAP! (Ambiente de Homologação) </h1>\nMBA! v3 o/"
