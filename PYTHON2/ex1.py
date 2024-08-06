valor = float(input("digite o valor da venda: "))
porc = valor * 10 / 100
pagvista = valor - porc
parcela = valor/3

comissao_avista = pagvista * 0.05
comissao_aprazo = valor * 0.05
print(f"compra com desconto {pagvista},\n parcelas: {parcela:.2f} \n comissao a vista: {comissao_avista}, \n comissao a prazo: {comissao_aprazo}")