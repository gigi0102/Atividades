avaliacao = int(input("digite o numero de avaliações: "))
notas = []
cont = 0

while cont < avaliacao:
    notas.append(float(input("digite a nota:")))
    cont = cont + 1
media = sum (notas) / len(notas)
print(media)