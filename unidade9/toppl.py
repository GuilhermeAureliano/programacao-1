# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def meu_in(inscritos, parametro):
    for e in inscritos:
        if parametro == e:
            return True
    return False

def filtra_alunos(alunos, inscritos, media):
    indices = []
    for i in range(len(alunos)):
        parametro = alunos[i][0]
        nota = alunos[i][1]
        if not meu_in(inscritos, parametro) or nota < media:
            indices.append(i)
    remov = 0
    for i in indices:
        alunos.pop(i - remov)
        remov += 1
    return remov

