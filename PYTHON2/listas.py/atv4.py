numero_avaliacoes = int(input("digite o numero de provas: "))
i = 0
soma = 0 
while i < numero_avaliacoes:
    soma += float(input("digite a nota: "))
    i = i + 1

media = soma / numero_avaliacoes
print(media)
