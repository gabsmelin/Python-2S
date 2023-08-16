import csv
from funcao import *

lista = []

with open("dados.csv", "r") as arquivos:
    dados = arquivos.readlines()

print(dados)

for linha in dados:
    lista = linha.split("|")

print(lista)