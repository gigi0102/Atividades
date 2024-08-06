sair = False
lista = []
lista_par = []

while sair != True:
    n = int(input("digite um numero: "))
    lista.append(n)

    if n % 2 == 0:
        lista_par.append(n)

    if n == 0:
        break

dados = sum(lista)
print(lista)
lista_par.pop()
print(lista_par)
  