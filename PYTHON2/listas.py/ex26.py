x = int(input("digite o valor da base: "))
y = int(input("digite o valor do expoente: "))

pot = 1
cont = 1

while cont <= y:
    pot *= x
    cont += 1 
print(f"(x) ^ (y) = (pot)")