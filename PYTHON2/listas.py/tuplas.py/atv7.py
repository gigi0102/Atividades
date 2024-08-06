matriz = [[11,2,11,13],[4,15,16,60],[7,8,19,200],[20,100,5,31]]

valor_maiores_10 = 0

for linha in matriz:
    for elemento in linha:
        if elemento > 10:
            valor_maiores_10 += 1

print(f"R= {valor_maiores_10} valores maiores que 10. ")
        

