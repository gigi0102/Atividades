class Pessoa:
    def __init__(self,nome,telefone,email,endereco):
         self.nome = nome
         self.telefone = telefone
         self.email = email
         self.endereco = endereco

    def Negociar(self):
         print("NEGOCIAÇÃO!")

class PessoaFisica(Pessoa):
     def __init__(self, nome, telefone, email, endereco,CPF):
          super().__init__(nome, telefone, email, endereco)
          self.CPF = CPF
     
     def Negociar(self):
         print("NEGOCIAÇÃO!")
    
     def PagarConta(self):
          print("Fui na loterica pagar minhas contas.")

class PessoaJuridica(Pessoa):
     def __init__(self, nome, telefone, email, endereco,CNPJ):
          super().__init__(nome, telefone, email, endereco)
          self.CNPJ = CNPJ
     
     def Negociar(self):
         print("NEGOCIAÇÃO!")

     def DeclararImposto(self):
          print(f"Meu CNPJ {self.CNPJ} esta inativo, preciso declarar meu imposto")

pessoa_fisica = PessoaFisica("Monica",12345678,"monica@email.com","Afonso Pena","123.456.789-00")
print(pessoa_fisica.nome)
print(pessoa_fisica.telefone)
print(pessoa_fisica.email)
print(pessoa_fisica.endereco)
print(pessoa_fisica.CPF)
     
