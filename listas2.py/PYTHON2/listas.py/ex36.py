alunos = 3
notas = 4

medias = []
media_sete = 0

for i in range(alunos):
    media = 0
    for j in range(notas):
        media += float(input(f"digite a nota {j+1} do aluno {i+1}: "))
    media /= notas
    medias.append(media)
    if media >= 7:
        media_sete += 1

print ("\n A media dps alunos foi: ")
for i in range(alunos):
    print(f"aluno {i+1}: {medias[i]}")

print(f"\n {media_sete} alunos tiveram media maior ou igual a 7.")