i = 0

lista_par = []
lista_impar = []
lista = []

while i < 20:
    n = int(input("digite um numero: "))
    lista.append(n)
    if i % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    i += 1
print(lista_impar)
print(lista_par)
       
  