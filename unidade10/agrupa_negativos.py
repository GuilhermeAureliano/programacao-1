# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def agrupa_negativos(lista):
    dict = {'nao-negativos': [], 'negativos': []}
    for e in lista:
        if e >= 0:
            dict['nao-negativos'] += [e]
        else:
            dict['negativos'] += [e]
    return dict
