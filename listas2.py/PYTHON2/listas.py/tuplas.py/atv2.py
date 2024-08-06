tupla = (1,2,3,4,5,6,7,8,9)
soma = 0
for i in tupla:
    if i % 2 == 0:
        soma += i
        print(i)
print(soma)