lab = float(input("digite sua nota de atv no laboratorio:"))
avBi = float(input("digite sua nota na avaliação bimestral:"))
exF = float(input("digite sua nota no exame final:"))

lb = 2
aV = 3
exFF = 5

x = (lab * lb)+(avBi*aV)+(exF*exFF)/lb+aV+exFF
m = x/6

if m >= 0 and m <= 2.9:
    print("aluno reprovado!")
elif m >= 3 and m <= 5.9:
    print("aluno de recuperação!")
else:
    print("aluno aprovado!")