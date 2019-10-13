# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def reducoes(seq):
    resultado = []
    for i in range(len(seq) - 1):
        red = int(seq[i]) - int(seq[i + 1])
        if red < 0:
            resultado.append(0)
        else:
            resultado.append(red)
    return resultado

