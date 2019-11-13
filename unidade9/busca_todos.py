# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def busca_matriz(m, e):
    indices = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == e:
                indices.append((i, j))

    return indices

