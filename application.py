from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hola FIAP! (Ambiente de produção) </h1>\nMBA! v4 o/"
