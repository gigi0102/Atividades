def argumentos(arg,*args):
    print("primeiro argumento: ",arg)
    for item in args:
        print("argumentp de *args",item)

argumentos("primeiro_argumento",'banana','laranja')