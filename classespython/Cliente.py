class Cliente:
    def __init__(self,nome,idade,fone,email):
        self._nome = nome
        self.idade= idade
        self.fone = fone
        self.email = email

    def comprar(self):
        print(f"{self._nome} realiza compras")

    def getNome(self):
        return self._nome

class ClientePremium(Cliente):
    def __init__(self, nome, idade, fone, email,areavip=True,desconto=20):
        super().__init__(nome, idade, fone, email)
        self.areavip = areavip
        self.desconto = desconto

    def comprar(self):
        print(f"{self._nome} compra muito com {self.desconto}% de desconto")



cliPremium = ClientePremium("Gisele",18,000000,"gigi@ortiz")
cliPremium.comprar()