salario = float(input("digite seu salario: "))
ano = 2019
ano_atual = int(input("digite o ano que voce esta: "))

aumento = 1.5 / 4000

while ano < ano_atual:
    ano += 1 
    salario *= 1 + aumento
    aumento *= 2

print(f"o salario em {ano} é de R$ {salario:.2f}")





