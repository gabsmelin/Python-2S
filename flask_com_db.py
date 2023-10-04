from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

#Criamos o APP
app = Flask(__name__)

#Jogamos uma API dentro do APP
api = Api(app)

#Passamos configurações direto para o app, para não afetar o código
##Passamos a API e passamos o nosso banco de dados como 'valor'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///1tdss.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "oracle+driver://username:password@host:port/dbname"  <--- Caso usamos o banco de dados da oracle
##Passamos um TRACK para 'salvar' alterações
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Usamos Model para instanciar um método, no caso ele está no App e por isso, a partir de agora db tem a classe model
db = SQLAlchemy(app)


#Usamos Model para instanciar um método
class Aluno(db.Model):
    #Passamos a tabela(e o nome dela) a ser seguida e em seguida seus parâmetros/colunas da tabela
    _tablename_= 'aluno'
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    nome = db.Column(db.Text, nullable = False)
    turma = db.Column(db.Text, nullable = False)
    obs = db.Column(db.Text, nullable = False)

    #Redefine o metódo reconstrutor da tabela
    def __init__(self, nome, turma, obs):
        self.nome = nome
        self.turma = turma
        self.obs = obs

#adiciona os dados a tabela
app.app_context().push()
#Cria uma nova tabela
db.create_all()


    
class Main(Resource):
    def get():
        #Pegamos todos os dados classe aluno
        alunos = Aluno.query.all()
        lista = []
        #Aqui alunos se transforma em aluno e fica organizado linha por linha, listando um aluno por vez.
        for aluno in alunos:
            print(aluno)
            #aqui damos append no dicionario(adicionamos coluna por coluna. ex: {("id": aluno.id, "nome": "Alberico", "turma"="1tdss", "obs":"Prof")}
            #fazemos isso para ficar um dicionario por linha, dentro de um json
            lista.append({'id': aluno.id, 'nome': aluno.nome, 'turma':aluno.turma, 'obs':aluno.obs})
        return jsonify(lista)
   

api.add_resource(Main, "/<nome>")

if __name__ == "__main__":
    app.run(port=8080)