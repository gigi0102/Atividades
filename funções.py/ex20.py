def imprimir_lista_numerada(lista):
    for i, elemento in enumerate(lista, start=1):
        print(f"{i}, {elemento}")

minha_lista = ["Pera", "Uva", "Maça", "Salada Mista"]
imprimir_lista_numerada(minha_lista)