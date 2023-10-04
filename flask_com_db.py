from flask import Flask
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
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.integer, unique= True)
    curso = db.Column(db.String)
    departamento = db.Column(db.String)

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
        pass
    def post():
        ...
    def put():
        ...
    def delete():
        ...
        

api.add_resource(Main, "/<nome>")

if __name__ == "__main__":
    app.run(port=8080)