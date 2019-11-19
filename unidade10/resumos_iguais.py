# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def agrupa_resumos_iguais(lista):
    resumo = {}
    for e in lista:
        iteragir = str(e)
        soma = 0
        for alg in iteragir:
            soma += int(alg)
        if soma not in resumo:
            resumo[soma] = []
    for e in lista:
        iteragir = str(e)
        soma = 0
        for alg in iteragir:
            soma += int(alg)
        for k in resumo.keys():
            if k == soma:
                resumo[k].append(e)
    return resumo
