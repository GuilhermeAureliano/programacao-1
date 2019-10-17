# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def divisor(num, lista):
    retorno = -1
    for i in range(len(lista)):
        if lista[i] % num == 0:
            retorno = i
            break
    return retorno
