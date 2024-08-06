alunos = [("Felipe",9.0),
          ("Manoel",6.0),
          ("Vitoria",10.0),
          ("Lucas",6.0)]


nota = []
for i in range (len(alunos)):
    print(alunos[i][1])
    
    if alunos[i-1][1] < alunos[i][1]:
        nota = alunos [i][1]
   
print(nota)