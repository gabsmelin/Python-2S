from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

lista = ["lucas"]

class Listar(Resource):
    def get(self):
        return str(lista)

class Main(Resource): 
    def post(self, nome):
        lista.append(str(nome).title())
        return f'Usúario { nome } foi adicionado com suceeso!'
    def delete(self, nome):
        if nome in lista:
            for index in range(0, len(lista)):
                if lista[index] == nome:
                    del lista[index]
                    return "Elemento removido!"
                else:
                    return "Elemento não existe!"
                
class Version(Resource):
    def get(self):
        return "0.0.1"
    

api.add_resource(Listar, "/")
api.add_resource(Main, "/<nome>")
api.add_resource(Version, "/version")