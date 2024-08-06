i = 0
soma = 0

while i < 10:
    try:
        num = int(input("digite um numero: "))
        soma += num
        i = i + 1
    except:
        print("ENTRADA INVALIDA! TENTE NOVAMENTE")

print("TOTAL: ",soma)