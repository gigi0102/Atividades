matriz = [[1,2,11,13],[4,15,16,60],[7,8,19,200],[20,100,5,3]]
l = 0
cl = 0
c = 0

for linha in range(4):
    for coluna in range(4):
        if matriz [linha] [coluna] > c:
            c = matriz [linha] [coluna]
            l = linha 
            cl = coluna

print(c,cl,l)