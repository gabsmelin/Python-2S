from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

lista = ["lucas"]

class listar(Resource):
    def get(self):
        return str(lista)

class Main(Resource): 
    def post(self, nome):
        lista.append(str(nome).title())
        return f'Usúario { nome } foi adicionado com suceeso!'
         