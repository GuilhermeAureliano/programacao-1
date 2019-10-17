# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def conta_alertas_acude(medicoes):
    alertas = 0
    for i in range(len(medicoes)):
        dif = abs(medicoes[i] - medicoes[i - 1])
        if dif < 10:
            if medicoes[i] < 17:
                alertas += 1
    return alertas
