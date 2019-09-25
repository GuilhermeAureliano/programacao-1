# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

chave = input()
N = int(input())

for e in range(N):
    frase = input()
    parametro = frase.split()

    for i in range(len(parametro)):
        if parametro[i] == chave:
            print(frase)

