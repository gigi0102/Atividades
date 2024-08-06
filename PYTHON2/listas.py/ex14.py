n = int(input("digite um numero: "))
cont = 0
lista = []
while cont < n:
    print(cont)
    
    if cont % 2 == 0:
        lista.append(cont)

    cont += 1

lista.sort()
print(lista)