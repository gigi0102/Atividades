tx = float(input("digite o imposto: "))
custo = float(input("digite o valor do produto: "))
def soma_imposto(tx,custo ):
    tx = tx/100
    custo = custo + (custo * tx)
    print(custo)

soma_imposto(tx,custo)
