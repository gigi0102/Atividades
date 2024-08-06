valor_inicial = int(input("digite o valor inicial: "))
valor_final = int(input("digite o valor final: "))

impar = []
if valor_inicial > valor_final:
    print("intervalo de valores invalido")
    
while valor_inicial < valor_final:
   
    if valor_inicial % 2 == 1:
        impar.append(valor_inicial)
        print(valor_inicial)
    valor_inicial += 1





soma = sum(impar)
print(soma) 