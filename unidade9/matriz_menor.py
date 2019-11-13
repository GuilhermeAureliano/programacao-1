# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def matriz_menor(m1, m2):
    matriz = []
    for i in range(len(m1)):
        dados = []
        for j in range(len(m1[0])):
            if m1[i][j] >= m2[i][j]:
                dados += [m2[i][j]]
            else:
                dados += [m1[i][j]]
        matriz += [dados]
    return matriz
