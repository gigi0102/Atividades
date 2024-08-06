class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterarPreco(self,novoPreco):
        self.novoPreco = novoPreco

    def mostrarSetor(self):
        print(f"Setor do ingresso: {self.setor} ")

class IngressoVIP(Ingresso):
    def __init__(self, preco, setor,camarote=False,openBar=False,openFood=False,estacionamento=False):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.openBar = openBar
        self.openFood = openFood
        self.estacionamento = estacionamento

    def pegarBebida(self):
        if self.openBar:
            print("Voce pode pegar bebidas no bar")
        else:
            print("Este ingresso nao inclui open bar")

    def acessarCamarote(self):
        if self.camarote:
            print("Voce tem acesso ao camarote.")
        else:
            print("Voce nao tem acesso ao camarote")

if __name__ == "__main__":
    ingressoNormal = Ingresso(preco=50.0,setor="Arquibancada") 
    ingressovip = IngressoVIP(preco=200.0,setor="VIP",camarote=True,openBar=True,openFood=True,estacionamento=True)

    ingressoNormal.mostrarSetor()
    ingressoNormal.alterarPreco(70.0)
    print(f"Novo preço do ingresso normal: R${ingressoNormal.preco:.2f}")

    ingressovip.mostrarSetor()
    ingressovip.pegarBebida()
    ingressovip.acessarCamarote()       
