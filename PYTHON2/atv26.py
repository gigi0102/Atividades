ano = int(input("digite um ano:"))

bis = ano %4

if bis == 0:
    print("o ano é bissexto")
else:
    print("o ano nao é bissexto")