def reverter_numero(numero):
    numero_str = str(numero)
    numero_revertido_str = numero_str[::-1]
    numero_revertido = int(numero_revertido_str)

    return numero_revertido

numero = int(input("digite um numero: " ))
print(reverter_numero(numero))