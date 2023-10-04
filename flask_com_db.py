from flask import Flask, jsonify, request
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
    def post(self):
        #data veio em json
        data =  request.get_json()
        #Checar se meus parametros estão dentro do JSON(Colunas/Campos)
        if "nome" in data and "turma" in data and "obs" in data:
            novo_alunos = Aluno(nome=data["nome"], turma=data["turma"], obs=data["obs"])
            db.session.add(novo_alunos)
            db.session.commit()
            return{"mensagem":"Aluno cadastrado com sucesso!"}, 201
        else:
            return{"mensagem":"Dadps incompletos"}, 400
    def put(self, id_aluno):
        #data veio em json
        data =  request.get_json()
        aluno = Aluno.query.get(id_aluno)
        #Checar se meus parametros estão dentro do JSON(Colunas/Campos)
        if aluno:
            if "nome" in data:
                aluno.nome = data["nome"]
            if "turma" in data:
                aluno.turma = data["turma"]
            if "obs" in data:
                aluno.obs = data["obs"]
            db.session.commit()
            return{"mensagem":"Aluno alterado com sucesso!"}, 200
        else:
            return{"mensagem":"Dadps incompletos"}, 404
    def delete(self, id_aluno):
        aluno = Aluno.query.get(id_aluno)
        if aluno:
            db.session.remove(aluno)
            db.session.commit()
            return {"message":"Aluno excluido com sucesso!"}, 200
        else:
            return {"message":"Aluno não encontrado."}, 404      
        

api.add_resource(Main, "/", "/<id_aluno>")

if __name__ == "__main__":
    app.run(port=8080)