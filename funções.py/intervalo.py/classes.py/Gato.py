class Gato:
    def __init__(self,nome,cor,peso):
        self.nome = nome
        self.cor = cor
        self.peso = peso

    def hello(self):
        print("Miaauuuu")


gato1 = Gato("Gato de botas","Laranja",5)
gato2 = Gato("Félix","Preto e branco",5)

gato2.hello()
gato1.nome = "Mingau"

print(gato2.nome)
print(gato2.cor)

print(f"{gato2.nome} é {gato2.cor} e tem {gato2.peso} kilos")