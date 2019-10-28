# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def separa_duas_cores(l1, cor1, cor2):
    for k in range(len(l1)):
        for i in range(len(l1) - 1):
            if l1[i] == cor2 and l1[i + 1] == cor1:
                l1[i], l1[i + 1] = l1[i + 1], l1[i]
