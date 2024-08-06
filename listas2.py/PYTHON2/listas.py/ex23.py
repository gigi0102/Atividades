i = 0

n = int(input("digite um numero: "))
lista = []

while i < n:
    i+=1
    if n % i == 0:
        lista.append(i)
lista.pop()
soma = sum(lista)
print(soma, lista)