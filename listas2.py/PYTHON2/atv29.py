idade = int(input("digite a idade do trabalhador: "))
tempo_de_servico = int(input("digite o tempo de serviço do trabalhador (em anos): "))

if idade >= 65 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
    print("o trabalhador pode se aposentar.")
else:
    print("o trabalhador nao pode se aposentar.")