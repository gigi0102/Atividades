idade = int(input("digite a idade do narrador: "))

if idade >= 5 and idade <= 12:
    categoria = "infantil"
elif idade > 12 and idade <= 17:
    categoria = "juvenil"
elif idade > 17:
    categoria = "senior"
else:
    categoria = "idade invalida"

print("categoria: ", categoria)