# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def cria_lista_presenca(turmas, nomes, k):
    matriculados = []
    for i in range(len(turmas)):
        if turmas[i] == k:
            matriculados.append(nomes[i])
    return matriculados
