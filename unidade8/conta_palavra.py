# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def conta_palavras(k, palavras):
    palavras = palavras.split(':')
    
    cont = 0
    for e in palavras:
        if len(e) >= k:
            cont += 1
    return cont
