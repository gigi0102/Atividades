def calcular_consumo_kwh(potencia_watts, tempo_horas):
    consumo_kwh = (potencia_watts / 1000) * tempo_horas
    return consumo_kwh
def calcular_conta_energia(consumo_kwh, valor_kwh):
    conta = consumo_kwh * valor_kwh
    return conta

potencia = 1500
tempo = 5
valor_kwh = 0.50

consumo = calcular_consumo_kwh(potencia , tempo)
conta = calcular_conta_energia(consumo , valor_kwh)

print(f"consumo: {consumo} Kwh")
print(f"conta de energia: R$ {conta}")