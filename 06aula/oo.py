class Inventario:
    def __init__(self, preco, qtd, dep) -> None:
        self.preco = preco
        self.qtd = qtd
        self.dep = dep
    def upper(self):
        self.preco = self.preco*0.9

if __name__ == "__main__":
    inventario1 = Inventario(5000, 3, "Pessoal")
    print("Preço: ", inventario1.preco, " | Quantidade: ", inventario1.qtd, " | Departamento: ", inventario1.dep)

    