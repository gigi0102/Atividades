class Produto:
    def __init__(self,nome,desc,preco,estoque):      
        self.nome = nome
        self.descricao = desc
        self.preco = preco
        self.qtde_estoque = estoque

    def getNome(self):
        print(f"PRODUTO: {self.nome}")

    def getEstoque(self):
        print(f"QUANTIDADE EM ESTOQUE: {self.qtde_estoque}")