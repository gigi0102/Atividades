vetor = [10,11,12,13,14,16,18,20]
i = 0
while i < 5:
    novo_valor = int(input("digite um novo valor: "))
    if novo_valor in vetor:
        print("este valor se encontra no vetor")
    else:
        vetor.append(novo_valor)

print(vetor)