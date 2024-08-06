valor_produto = float(input("digite o valor do produto: "))
estado_destino = input("digite o estado destino do produto (MG, SP, RJ, MS): ")

taxas_imposto = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

if estado_destino in taxas_imposto:
    taxas_imposto = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + taxas_imposto)
    print("o preço final do produto para o estado ",estado_destino, "é: R$", preco_final)
else:
    print("ERRO: ESTADO DESTINO INVALIDO")