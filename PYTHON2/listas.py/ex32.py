num = []
x = 0

while x < 5:
    n = int(input("digite um numero: "))
    num.append(n)
    x += 1

i = 0

while i < 5:
    print(num[i])
    i += 1

soma = sum(num)
print("a soma é: ",soma)