# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def transposta(M):
    tmatriz = [[0 for l in range(len(M))] for c in range(len(M[0]))]

    for i  in range(len(M[0])):
        for j in range(len(M)):
            tmatriz[i][j] = M[j][i]
    return tmatriz
