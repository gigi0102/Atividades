class Passagem:
    def __init__ (self,preco,assento):
        self.preco = preco
        self.assento = assento
    def alterarPreco(self,novoPreco):
        self.novoPreco = novoPreco
        return self.novoPreco
    
    def EscolherAssento(self):
        return self.assento
    
class PassagemAviao(Passagem):
    def __init__(self, preco, assento,portaodeembarque,checkin):
        super().__init__(preco, assento)
        self.portaodeembarque = portaodeembarque
        self.checkin = checkin
    
    def Decolar(self):
        print("O AVIÃO DECOLOU!!!")
    def Abastecer(self):
        print("O AVIÃO PRECISA ABASTECER") 

class PassagemBus(Passagem):
    def __init__(self, preco, assento,placa,leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito
    
    def Decolar(self):
        print("O ONIBUS PARTIU!!!")
    def Abastecer(self):
        print("O ONIBUS PRECISA ABASTECER")    
        
passagem = PassagemAviao(2000,20,3,"este é o meu assento")
print(f"O preço da passagem é : {passagem.preco}")
print(f"O seu Assento é : {passagem.assento}")
print(f"O seu portao de embarque é : {passagem.portaodeembarque}")
print(f"O seu checkin é {passagem.checkin}")
print(passagem.Decolar())
print(passagem.Abastecer())
 
 
passagem2 = PassagemBus(113,10,1323321,21)
print(f"O preço da sua passagem é : {passagem2.preco}")
print(f"O seu assento é {passagem2.assento}")
print(f"A placa do BUS é {passagem2.placa}")
print(f"O seu leito é {passagem2.leito}")
print(passagem2.Decolar())
print(passagem2.Abastecer())
 
      