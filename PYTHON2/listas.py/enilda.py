info = []

nome = str(input("digite seu nome: "))

info.append(nome)

email = str(input("digite seu email: "))

info.append(email)

senha = str(input("digite sua senha: "))

info.append(senha)
print(info)       

produto = []

nome_produto = str(input("digite o nome do produto cadastrado: "))

produto.append(nome_produto)
print(produto)

valor = float(input("qual o valor do produto? "))

produto.append(valor)
print(valor)

quantidade = int(input("qual a quantidade do produto? "))

produto.append(quantidade)
print(quantidade)

print(produto)

venda = int(input("quantos produtos deseja? "))

valor = produto[1] * venda
sub = produto[2] - venda

produto.insert(2,sub)
produto.pop()
print(produto)
print(valor)