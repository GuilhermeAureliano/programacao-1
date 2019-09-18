# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

cont = 0
inicio = 15.2

for i in range(14):

    if cont == 0:
        print(inicio)
        cont += 1
    
    inicio += -1.5
    print('%.1f' % inicio)
