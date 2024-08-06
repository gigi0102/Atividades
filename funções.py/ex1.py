def potencia(base,expoente):
    resultado = base ** expoente
    return resultado

base = int(input("digite a base :"))
expoente = int(input("digite o expoente: "))

print(f"{base} elevado a {expoente} é {potencia(base,expoente)}")


  