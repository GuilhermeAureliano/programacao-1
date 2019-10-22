# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def SelectionSort(lista):
    for indice in range(0, len(lista)):
        minimo = indice
        for j in range(indice + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[indice], lista[minimo] = lista[minimo], lista[indice]
    return lista

assert SelectionSort([-2, 9, 5, 7, 5, 2, 1, 4]) == [-2, 1, 2, 4, 5, 5, 7, 9]
