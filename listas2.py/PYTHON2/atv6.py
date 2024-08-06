print("qual turno voce estuda?")
print("'M' para matutino")
print("'V' para vespertino")
print("'N' para noturno")
print("qualquer outra letra nao sera valido!")
turno = str(input("digite o turno: "))

if turno == 'M' or turno == 'm':
    print("BOM DIA!")
elif turno == 'V' or turno =='v':
    print("BOA TARDE!")
elif turno == 'N' or turno == 'n':
    print("BOA NOITE!") 
else:
    print("opção invalida, digite novamente")