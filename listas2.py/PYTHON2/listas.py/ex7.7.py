lista = []

for i in range(10):
    i+= 1
    lista.append(int(input("valor: ")))

media = sum (lista) / len(lista)
print(media)