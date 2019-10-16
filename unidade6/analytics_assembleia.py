# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def conta_votos(votacoes, id_votacao):
    sim = nao = 0
    for i in range(len(votacoes)):
        votacao = votacoes[i].split(',')
        for j in range(len(votacao)):
            if votacao[j] == str(id_votacao):
                if votacao[j - 1] == 'sim':
                    sim += 1
                else:
                    nao += 1
    votos = []
    votos.append(sim)
    votos.append(nao)
    return votos

