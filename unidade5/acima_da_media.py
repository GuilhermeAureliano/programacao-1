# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

mensal = float(input())

maior = 0
seq = ''

while True:
    sequencia = input()
    lista = sequencia.split()

    if lista[0] == 'fim':
        break

    soma = 0
    for i in range(len(lista)):
        soma += float(lista[i])

    media = soma / len(lista)

    if (media * 2 ) < mensal:
        break
    
    if media  > mensal:
        seq = sequencia
        print(seq)
