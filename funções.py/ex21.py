def lista_argumento(lista):
    if not lista:
        return 0
    soma = sum(lista)
    media = soma / len(lista)
    return media

minha_lista = [10,100,20,2000]
media = lista_argumento(minha_lista)
print(f"A media é: {media}")