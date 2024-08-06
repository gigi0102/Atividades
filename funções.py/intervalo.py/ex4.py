def world_cup_titles(country,*args):
    print('País:',country)
    for título in args:
        print('Ano: ',título)

país = "Brasil"

world_cup_titles("BRASIL",1958,1962,1970,1994,2002)