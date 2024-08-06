def salario(salario,hr_trabalhada):
    if hr_trabalhada <= 40:
        n1 = 35.3 * hr_trabalhada
        print(f"o seu salario é: {n1}")
    elif hr_trabalhada > 40:
        n2 = hr_trabalhada - 40
        res = n2 * 17.65
        n3 = res + salario 
        print(f"o seu salario é: {n3}")

salario = 1412.00
hr_trabalhada = int(input("digite a quantidade de hrs trabalhada:"))
salario(salario,hr_trabalhada)