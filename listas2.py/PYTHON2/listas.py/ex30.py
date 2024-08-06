valor_inicial = 2
valor_final = 50

impar = []

while valor_inicial < valor_final:
   
    if valor_inicial % 2 == 1:
        impar.append(valor_inicial)
        print(valor_inicial)
    valor_inicial += 1

soma = sum(impar)
print(soma)