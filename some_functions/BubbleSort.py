# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def BubbleSort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

assert BubbleSort([-2, 9, 5, 7, 5, 2, 1, 4]) == [-2, 1, 2, 4, 5, 5, 7, 9]
