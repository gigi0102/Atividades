class Filme:
    def __init__(self,nome,duração):
        self.nome = nome
        self.duração = duração
    def Play(self):
        print(f"o filme {self.nome} foi dado play")
class Suspense(Filme):
    def __init__(self, nome, duração):
        super().__init__(nome, duração)
    
    def explodir(self):
        print(f"o filme {self.nome} é sinistro")


filme = Suspense("Os Suspeitos","130min")
print(filme.Play)
print(filme.explodir())
print(filme.duração)