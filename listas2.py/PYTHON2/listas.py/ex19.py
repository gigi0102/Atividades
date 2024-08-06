numero = int(input("Digite o número entre 100 e 9999: "))

while(numero < 100 or numero > 9999):

       print(f'Número {numero} invalido, digite novamente.')

       numero = int(input("Digite o número entre 100 e 9999: "))

centenas = numero//100

dezenas = (numero - centenas*100)//10

unidades = numero - (centenas*100 + dezenas*10)

print(f'O número {numero} equivale a {centenas*100} + {dezenas*10} + {unidades}')