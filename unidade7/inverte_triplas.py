# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def inverte3a3(string):
    lista, cont, s = [], 0, ''

    for i in range(len(string)):
        s += string[i]
        cont += 1
        if cont == 3:
            lista.append(s) # Adiciona de 3 em 3 na lista
            cont, s = 0, ''

    retorno = ''
    for i in range(len(lista) -1, -1, -1):
        retorno += lista[i]
    return retorno
