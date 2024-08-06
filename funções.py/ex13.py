km = int(input("digite a distancia em km: "))
l = int(input("digite a quantidade de litros de gasolina consumidos: "))
cal = km/l
def consumo(cal):
    if cal <= 8:
        print("gasta muito")
    elif cal > 8 and cal < 15:
        print("economico")
    elif cal >15:
        print("super economico")
consumo(cal)