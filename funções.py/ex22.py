def criar_lista_padroes(quantidade, valor_padrao):
    return [valor_padrao] * quantidade

quantidade = 10
valor_padrao = 5
lista = criar_lista_padroes(quantidade, valor_padrao)

print(lista)