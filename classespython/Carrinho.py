class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserirprodutos(self,produtos):
        self.produtos.append(produtos)

    def listarprodutos(self):
        for prod in self.produtos:
            print(f"Nome: {prod.nome} Preço: {prod.preco}")