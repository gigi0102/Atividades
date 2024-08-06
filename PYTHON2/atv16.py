hora = 40.50
hora_trab = int(input("digite as horas trabalhadas: "))
total = hora*hora_trab

if total >= 2500:

    imposto = total - (total*0.11)
    print(f"salario bruto R$ {total}\n salario liquido R$ {imposto}")