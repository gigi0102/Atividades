distancia_km = float(input("digite a distancia percorrida em quilometros: ")) 
litros_gasolina = float(input("digite a quantidade de litros de gasolina consumidos: " ))

consumo_km_por_litro = distancia_km / litros_gasolina

if consumo_km_por_litro < 8:
    mensagem = "venda o carro!"
elif consumo_km_por_litro >= 8 and consumo_km_por_litro <= 14:
    mensagem = "economico!"
else:
    mensagem = "super economico!"

print("consumo: ",mensagem)