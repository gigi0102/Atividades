class Pessoa:
    def __init__(self,matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self,matricula,nome,idade,notas):
        super().__init__(matricula,nome,idade)
        self.notas = notas
        self.nome = nome
    def calcularMedia(self):
        if self.notas:
            media = sum(self.notas) / len(self.notas)
            return media
        else:
            return 0
    def estudar(self):
        print(f"O aluno {self.nome} esta estudando")
    
        
class Professor(Pessoa):
    def __init__(self,matricula,nome,idade,formacao,disciplina,cargaHoraria,salario):
        super().__init__(matricula,nome,idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.cargaHoraria = cargaHoraria
        self.salario = salario
        self.nome = nome
    def lecionar(self):
        print(f"O professor {self.nome} esta lecionando a disciplina de {self.disciplina}")
    def calcularSalarioAnual(self):
        salarioAnual = self.salario * 12
        return salarioAnual

if __name__ == "__main__":
    aluno1 = Aluno(matricula="A001",nome="Maria",idade=18,notas=[8,8,7,9,10])
    professor1 = Professor(matricula="B1002",nome="Junior",idade=54,formacao="Mestrado",disciplina="Historia",cargaHoraria=12,salario=5000)

    print(f"Media do aluno {aluno1.nome}: {aluno1.calcularMedia()}")
    aluno1.estudar()

    professor1.lecionar()
    print(f"Salario anual do professor {professor1.nome}: R${professor1.calcularSalarioAnual():.2f}") 

