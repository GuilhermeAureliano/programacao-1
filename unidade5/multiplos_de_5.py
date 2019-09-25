# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

n = int(input())
cont = 0

while True:
    if cont == n:
        break
    else:
        saida = 0
        if cont % 5 == 0:
            saida += 1   
        if cont % 2 == 0:
            saida += 1
        if cont < n:
            saida += 1

    if saida == 3 and cont != 0:
        print(cont)
    cont += 1

            


