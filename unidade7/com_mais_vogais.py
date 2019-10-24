# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def remove_palavras_com_mais_vogais(lista1):
    maior = float('-inf')
    vg = 0
    vogais = 'aeiouAEIOU'
    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            e = lista1[i][j]
            if e in vogais:
                vg += 1
        if vg > maior:
            maior = vg
        vg = 0
    cont = 0
    indices = []
    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            e = lista1[i][j]
            if e in vogais:
                cont += 1
        if cont >= maior:
            indices.append(i)
        cont = 0
    pos = 0
    for i in indices:
        lista1.pop(i - pos)
        pos += 1


