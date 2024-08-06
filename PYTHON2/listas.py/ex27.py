a = int(input("digite o valor inicial: "))

cont = 1
resultado = 1

while (cont <= a):
    resultado *= cont
    cont += 1
print(f"o fatorial de {a} é: {resultado}")