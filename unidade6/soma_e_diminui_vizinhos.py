# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def soma_diminui_vizinhos(lista):
    for i in range(len(lista)):
        if i > 0:
            if i % 2 == 0:
                lista[i] = (lista[i] * - 1)
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma
