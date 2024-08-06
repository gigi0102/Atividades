salario_atual = float(input("digite o salario atual do funcionario: "))
tempo_servico = int(input("digite o tempo de serviço do funcionario (em anos): "))

if salario_atual < 1000:
    aumento = salario_atual * 0.2
else:
    aumento = salario_atual * 0.1
if tempo_servico >= 10:
    bonus = 500 
elif tempo_servico >= 5:
    bonus = 300
else:
    bonus = 200

novo_salario = salario_atual + aumento + bonus

print("o novo salario do funcionario é: ",novo_salario)