# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def filtra_urls(lista):
    retorno = []
    for i in range(len(lista)):
        for j in range(len(lista[i]) - 1):
            if lista[i][j] == '.' and lista[i][j + 1] == 'g' and lista[i][j + 2] == 'o' and lista[i][j + 3] == 'o' and lista[i][j + 4] == 'g' and lista[i][j + 5] == 'l' and lista[i][j + 6] == 'e':
                retorno.append(lista[i])
    return retorno
