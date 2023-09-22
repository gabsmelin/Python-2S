class Inventario:
    def __init__(self, preco, qtd, dep):
        self.__preco = preco
        self.qtd = qtd
        self.dep = dep

        
    def depreciar(self):
        self.__preco = self.preco*0.9


    def get_preco(self):
        return self.__preco
    

    def set_preco(self, preco):
        self.__preco = preco


if __name__ == "__main__":
    inventario1 = Inventario(5000, 2, "Pessoal")
    inventario1.set_preco(3000)
    print(inventario1.get_preco())  