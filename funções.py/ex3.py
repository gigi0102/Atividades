def verifica_positivo_negativo(numero):
    if numero > 0:
        return "1"
    else:
        numero < 0
        return "-1"
    
entradausuario = float(input("digite um numero: "))
resultado = verifica_positivo_negativo(entradausuario)

print(f"o resultado é: {resultado}")