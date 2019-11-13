# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def coluna(matriz, i):
    retorno = []
    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            if c == i:
                retorno += [matriz[l][i]]
    return retorno
