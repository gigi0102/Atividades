i = 0 
lista = []
#num = int(input("digite um numero: "))

x = 0
while x < 100:
    x = x+1
    if x % 2 == 0:
       lista.append(x)

print(lista)

soma = sum(lista)
print(soma)

