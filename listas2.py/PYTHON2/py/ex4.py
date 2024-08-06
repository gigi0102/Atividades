def argumento(numero):
    if numero > 0 :
        return "P"
    else:
        return "N"
    
entrada_usuario = float(input("digite um número: "))
res = argumento(entrada_usuario)
print(f"o resultado é {res}")