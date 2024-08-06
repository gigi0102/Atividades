i = 0
lista_num = []

qtd_num = int(input('Entre com a quantidade de números a serem lidos: '))

while i < qtd_num:
    num = int(input('Digite um número: '))
    i += 1
    lista_num.append(num)

print(f'O maior valor é: {max(lista_num)}')