# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def busca(seq, valor):
    indice = -1
    for i in range(len(seq)):
        if seq[i] == valor:
            indice = i
            break
    return indice
