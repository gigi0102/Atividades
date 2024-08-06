import math

class Pessoa:
    def __init__(self,nome,ano_nasc):
        self.name = nome 
        self.idade =  2024 - ano_nasc

    def mostrarIdade(self):
        return self.idade 
    
    def mostrarQualidade(self,quali):
        return f"{self.nome} é muito {quali}"
    
p1 = Pessoa("Thiago",1986)

print( p1.mostrarIdade())

