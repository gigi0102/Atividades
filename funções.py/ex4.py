def converte_para_segundos(horas,minutos,segundos):
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos

horas = 1
minutos = 30
segundos = 15
resultado = converte_para_segundos(horas,minutos,segundos)
print(f"{horas} horas, {minutos} minutos e {segundos} segundos são {resultado} segundos.")