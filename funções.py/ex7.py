import math

def calculo_volume_esfera(raio):
    volume = (4/3) * math.pi * raio ** 3
    return volume

if __name__ == "__main__":
    raio_teste = 5
    volume = calculo_volume_esfera(raio_teste)
    print(f"o volume de uma esfera com raio {raio_teste} é {volume:.2f}")
