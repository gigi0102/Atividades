salario = 1412
emprestimo = float(input("digite o valor que deseja o emprestimo:"))

desc = salario*0.2

if emprestimo >= desc:
    print("emprestimo nao pode ser concedido, valor acima do minimo!")
else:
    print("emprestimo concedido!")