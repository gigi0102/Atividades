n1 = float(input("digite a primeira nota : "))
n2 = float(input("digite a segunda nota : "))

if (n1 <= 0 or n1 >=0) or (n2 <= 0 or n2 >=0 ):
    print("notas validas ")
else :
    print("notas invalidas ")
    media = (n1 + n2 ) / 2
    print(f"a sua media é : {media}")