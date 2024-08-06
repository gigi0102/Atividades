class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def BaterPonto(self):
        self.pontos.append(1)
        print(f"Ponto batido pelo funcionario {self.nome}. Pontos: {self.pontos}")

class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario,comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
        self.metaBatida = False
    def baterMeta(self):
        self.metaBatida = True
        print(f"Meta batida pelo vendedor {self.nome}. Comissao: {self.comissao}")

class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario,senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha
    
    def autenticar(self,senha):
        if self.senha == senha:
            print(f"Autenticação bem-sucedida para o gerente {self.nome}")
            return True
        else:
            print(f"Autenticação falhou para o gerente {self.nome}")
            return False
        

vendedor = Vendedor("Felipe","234",8000,400)
vendedor.BaterPonto()
vendedor.baterMeta()

gerente = Gerente("Sofia","980",3000,"senha098")
gerente.BaterPonto()
gerente.autenticar("senha098")