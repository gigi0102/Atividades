valor_venda = float(input("digite o valor da venda: "))

if valor_venda >=100000:
    comissao = 700 + (0.16 * valor_venda)
elif valor_venda >= 80000:
    comissao = 650 + (0.14 * valor_venda)
elif valor_venda >= 60000:
    comissao = 600 + (0.14 * valor_venda)
elif valor_venda >= 40000:
    comissao = 550 + (0.14 * valor_venda)
elif valor_venda >= 20000:
    comissao = 500 + (0.14 * valor_venda)
else:
    comissao = 400 + (0.14 * valor_venda)

print("a comissao a ser paga ao vendedor é: ",comissao)