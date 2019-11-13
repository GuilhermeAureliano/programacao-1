# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def abaixo(m, acm, abx):
    if abx > acm:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i > 0:
                    if j < i:
                        m[i][j] = 0
def acima(m, acm, abx):
    if acm > abx:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if j > i:
                    m[i][j] = 0
def iguais(m, acm, abx):
    if acm == abx:
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i != j:
                    m[i][j] = 0
def zera_acima_ou_abaixo(m):
    acm, abx = 0, 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if j > i :
                acm += m[i][j]
            if i > 0:
                if j < i:
                    abx += m[i][j]
    abaixo(m, acm, abx)
    acima(m, acm, abx)
    iguais(m, acm, abx)
    return m
