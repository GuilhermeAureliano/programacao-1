# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def inverte2a2_condicional(seq):
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            if i % 2 == 0:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
    return seq

