# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def top_3(lista):
    for indice in range(3):
        maior = indice
        for i in range(indice, len(lista)):
            if lista[i] > lista[maior]:
                maior = i
        lista[indice], lista[maior] = lista[maior], lista[indice]
    return lista
