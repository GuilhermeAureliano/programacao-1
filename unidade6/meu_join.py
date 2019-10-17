# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def meu_join(sep, entrada):
    join = ''
    for i in range(len(entrada)):
        if i != len(entrada) - 1:
            join += entrada[i] + sep
        else:
            join += entrada[i]
    return join
