n1 = int(input("digite um numero: "))
n2 = int(input("digite outro numero: "))

soma = 0
mult = 1

while n1 <= n2:
    if n1 % 2 == 0:
        soma += n1
        n1 = n1 + 1
    else:
        mult *= n1
        n1 += 1

print(soma)
print(mult)