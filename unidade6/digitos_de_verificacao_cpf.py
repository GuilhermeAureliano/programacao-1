# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def calcula_digitos_verificacao(entrada):
    cont = 10
    soma = 0
    for i in range(len(entrada)):
        soma += int(entrada[i]) * cont
        cont -= 1
    dg1 = (10 * soma) % 11
    if dg1 == 10:
        dg1 = 0
    entrada = entrada + str(dg1)
    cont2 = 11
    soma2 = 0
    for i in range(len(entrada)):
        soma2 += int(entrada[i]) * cont2
        cont2 -= 1
    dg2 = (10 * soma2) % 11
    if dg2 == 10:
        dg = 0
    resultado = str(dg1) + str(dg2)
    return resultado
