#2ºSemestre-Revisão

#Lista
##Salvamos valores dentro delas. É uma estrutura posicional.
lista=["A", "B"]

#Dicionario
##É uma lista com chave-valor.
dicionario = {"pf8945":{"nome":"jandiro",  "cargo":"professor", "curso":"tds"},"pf1245":{"nome":"alberico",  "cargo":"professor", "curso":"adm"},"pf1495":{"nome":"henrico",  "cargo":"professor", "curso":"cyber"}}

#Busca
##Dentro desta chave-valor pode fazer referência a uma estrutura. Para buscarmos determinado chave
##Jeito Básico
#print(dicionario["pf1245"]["nome"])

##Jeito Inventario
def relatorioDados():
    for index, lista in dicionario.items():
        print("ID:................." + index)
        print("Nome:..............." + lista["nome"])
        print("Cargo:.............." + lista["cargo"])
        print("Curso:.............." + lista["curso"])
        print("\n")




#Adicionar
##Adicionar um novo dado. Obs: []-> dados, {}->nova chave
#chave = input("Entre com a chave: ")
#dicionario[chave] = {"nome": "Ronqui", "cargo": "Coordenador", "curso":"TDS"}#[chave onde vamos adicionar]/[passa o que quiser, dados a serem adicionados]
#print(dicionario)

##Jeito Inventário
def adicionar(): 
    chave = input("Entre com a chave: ")
    dicionario[chave] = [input("Adicione um nome: "),
                        input("Adicione um cargo: "),
                        input("Adicione um turma: ")]


adicionar()
relatorioDados()


