from flask import Flask, render_template## <-- função que nos permite trazer conteúdos que está em um arquivo
import datetime

app = Flask(__name__)

@app.route("/")##através da "extensão" flask podemos acessar nosso conteúdo
def index():
    return render_template("index.html")##importando arquivo 

@app.route("/about")
def about():
    return render_template("about.html", tempo=datetime.datetime.utcnow())

if __name__ == "__main__":##Só roda se eu partir do arquivo inicial
    app.run(host="localhost", port=8080)