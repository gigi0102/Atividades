from Produto import Produto
from Carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()

p1 = Produto("Iphone 14",9800,80)
p2 = Produto("Capinha de celular",50,1000)
p3 = Produto("Fone sem fio",300,200)

car.inserirprodutos(p1)
car.inserirprodutos(p2)
car.inserirprodutos(p3)

car.listarprodutos()