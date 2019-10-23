# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def is_substring(str1, str2):
    retorno = False
    cont = 0
    for i in range(len(str1)):
        if str1[i] == str2[cont]:
            cont += 1
        else:
            cont = 0
        if cont == len(str2):
            retorno = True
            break
    return retorno
