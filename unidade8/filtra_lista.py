# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def  filtra_lista(num, lista):
    indexes = []
    for i in range(len(lista)):
        if i % num == 0:
            indexes.append(lista[i])
    return indexes
