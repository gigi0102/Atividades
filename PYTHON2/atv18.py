peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

homens = (72.7*altura)-58
mulheres = (62.1*altura)-44.7

print(f"peso ideal dos respectivos sexos: \n homens: {homens:.2f}kg\n mulheres: {mulheres:.2f}kg")