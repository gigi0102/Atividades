cardapio = {
    100: 12.00,
    102: 18.50,
    103: 25.50,
    104: 17.00,
    105: 9.50,
    106: 6.00
}

codigo_produto = int(input("digite o codigo do produto: "))
quantidade = int(input("digite a quantidade desejada: "))

if codigo_produto in cardapio:
    preco_unitario = cardapio[codigo_produto]
    preco_total = preco_unitario * quantidade
    print("total a pagar: ", preco_total)
else:
    print("codigo de produto invalido.")