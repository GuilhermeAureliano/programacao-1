# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def filtra_divisores(lista1):
    def meu_sum(lista1):
        div = []
        for i in range(len(lista1)):
            soma = 0
            lista1[i] = str(lista1[i])
            for j in range(len(lista1[i])):
                soma += int(lista1[i][j])
            div.append(soma)
        return div
    indices = []
    somatorio = meu_sum(lista1)
    for i in range(len(lista1)):
        lista1[i] = int(lista1[i])
        if lista1[i] % somatorio[i] != 0:
            indices.append(i)
    cont = 0
    for i in indices:
        lista1.pop(i - cont)
        cont += 1
