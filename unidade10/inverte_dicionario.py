# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def inverte_dicionario(dicionario):
    inverso = {}
    for k, v in dicionario.items():
        if v not in inverso.keys():
            inverso[v] = []
    for k, v in dicionario.items():
        if v in inverso.keys():
            inverso[v].append(k)
    for v in inverso.values():
        for indice in range(0, len(v)):
            minimo = indice
            for j in range(indice + 1, len(v)):
                if v[j] < v[minimo]:
                    minimo = j
            v[indice], v[minimo] = v[minimo], v[indice]
    return inverso
