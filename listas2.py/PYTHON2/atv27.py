n1 = float(input("digite um lado: "))
n2 = float(input("digite outro lado: "))
n3 = float(input("digite outro lado: "))

if n1 == n2 == n3 :
    print("TRIANGULO EQUILATERO!")
elif n1 == n2 or n2 == n3 or n1 == n3 :
    print("TRIANGULO ISOCELES!")
elif n1 != n2 != n3:
    print("TRIANGULO ESCALENO!")
else:
    print("NÃO É TRIANGULO.")