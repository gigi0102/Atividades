n = 3
m = 3

matriz = []
for linha in range(n): 
    lin = []
    for col in range(m):
        lin.append(int(input("digite um valor: ")))
    matriz.append(lin)

print(matriz)
for i in matriz:
    print(i)