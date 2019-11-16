# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def time_campeao(dados):
    retorno = []
    campeao = -1
    for k in dados.keys():
        pontos = dados[k][0]
        if pontos >= campeao:
            if retorno and pontos > campeao:
                retorno.pop()
                retorno.append(k)
            else:
                retorno.append(k)
            campeao = pontos
    return retorno
