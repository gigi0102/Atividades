numeros = [4,5,6,7,8,9]
print(numeros)
numeros.append(1.2)
numeros.append(2.0)
numeros.append(3.5)
numeros.append(4.5)
numeros.append(5.5)
numeros.append(6.6)
print(numeros)

numeros.pop(5)
numeros.pop(6)
print(numeros)

numeros.insert(1,10)
numeros.insert(2,11)
print(len(numeros))
print(max(numeros))
print(min(numeros))
print(sum(numeros))
print(sum(numeros) / len(numeros))

print(numeros)
numeros.remove(10)
print(numeros)
print(numeros.index(11))

print(numeros[4]*numeros[5])
print(sorted(numeros,reverse=True ))