produto = float(input("digite o valor de aquisicao deste produto:"))

if produto <=50:
    desc = produto+(produto*0.45)
    print(f"o produto sera vendido com o reajuste por {desc:.2f}")
elif produto >=50:
    desc = produto+(produto*0.3)
    print(f"o produto podera ser vendido com o reajuste por R${desc:.2f}")
