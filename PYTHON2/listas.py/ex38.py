num = int(input("digite um numero: "))
soma = 0
for num in range (2, num + 1):
    primo = True
    for i in range(2,num):
        if num % i == 0:
            primo = False
    if primo:
        print(num)
        soma += num
print(soma)
