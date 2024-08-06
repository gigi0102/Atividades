preco_antigo = float(input("digite o preço antigo do produto: "))

if preco_antigo <= 50:
    percentual_aumento = 0.05
elif preco_antigo <= 100:
    percentual_aumento = 0.10
else:
    percentual_aumento = 0.15

preco_novo = preco_antigo * (1 + percentual_aumento)

print("o preço novo do produto é: ", preco_novo)

if preco_novo <= 80:
    mensagem = "barato"
elif preco_novo <= 120:
    mensagem = "normal"
else:
    mensagem = "caro"

print("mensagem: ",mensagem)