class Cliente:
    def __init__(self,nome,idade):      
        self.nome = nome
        self.idade = idade

    def getNome(self):
        print(f"Nome: {self.nome}")

    def getIdade(self):
        print(f"Idade: {self.idade}")