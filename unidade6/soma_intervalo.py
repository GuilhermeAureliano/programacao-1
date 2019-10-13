# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def soma_intervalo(a, b):
    soma = 0
    cont = a
    lim = b
    while True:
        soma += cont
        cont += 1
        if cont == (lim + 1): break
    return soma


