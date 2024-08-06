print("escolha a opção: ")
print("1- soma de 2 numeros")
print("2- diferença entre 2 numeros (maior pelo maior). ")
print("3- produto entre dois numeros")
print("4- divisão entre 2 numeros (o denominador nao pode ser zero).")

opcao = input("digite o numero da operação desejada: ")

n1 = float(input("digite o primeiro numero: "))
n2 = float(input("digite o segundo numero: "))

if opcao == '1':
    print("resultado: ", n1+n2)
elif opcao == '2':
    print("resultado: ", abs(n1-n2))
elif opcao == '3':
    print("resultado: ", n1*n2)
elif opcao == '4':
    if n2 != 0:
        print("resultado: ",n1/n2)
    else:
        print("ERRO: NAO E POSSIVEL DIVIDIR POR ZERO.")
else:
    print("OPCAO INVALIDA. POR FAVOR, ESCOLHA UMA OPÇÃO DE 1 A 4.")