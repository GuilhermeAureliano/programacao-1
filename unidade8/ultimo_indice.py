# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def ultimo_indice(num, lista):
    index = 0
    cont = False
    for i in range(len(lista)):
        if lista[i] == num:
            if i >= index:
                index = i
                cont = True
    if cont == False:
        return -1
    else:
        return index
