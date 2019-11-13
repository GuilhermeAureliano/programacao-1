# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def diagonais(M):
    retorno = []
    ds, dp = [], []
    for i in range(len(M)):
        ds.append(M[i][-i-1])
        for j in range(len(M[0])):
            if i == j:
                dp.append(M[i][j])
    retorno += [dp]
    retorno += [ds]
    return retorno

