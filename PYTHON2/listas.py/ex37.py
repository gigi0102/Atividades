num = int(input("digite um numero: "))
cont = 1
soma = 0

while cont < (num+1):
    
    if num % cont == 0:
      soma += 1

    cont += 1 

if soma == 2:
  print(num , "é primo")
else:
  print(num, "nao é primo")
        