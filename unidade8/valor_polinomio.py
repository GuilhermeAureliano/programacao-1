# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def valor_polinomio(polinomio, valor):
    soma = 0
    for i in range(len(polinomio)):
        soma += polinomio[i] * (valor ** i)
    return soma
