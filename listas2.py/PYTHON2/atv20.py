n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

p1 = n1 *1
p2 = n2 *1
p3 = n3 *2

x = (n1*p1) + (n2*p2) + (n3*p3)/p1+p2+p3

if x >= 60:
    print("aluno aprovado!")
else:
    print("aluno reprovado!")