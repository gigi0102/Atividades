i = 0

lista3 = []

while i < 1000:
    i+=1
    if i % 5 == 0:
        lista3.append(i)
    if i % 3 == 0:
        lista3.append(i)
soma = sum(lista3)
print(soma)