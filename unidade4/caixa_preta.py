# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

N = int(input())
lista = []
validos = 0
invalido = 0

for i in range(N):
    dados = input().split()

    if invalido == 0: 
        for e in range(len(dados)):
            if int(dados[e]) >= 0:
                validos += 1
            else:
                break

    if invalido == 0:
        if int(dados[0]) < 0:
            print('dado inconsistente. peso negativo.')
            invalido += 1

        elif int(dados[1]) < 0:
            print('dado inconsistente. combustível negativo.')
            invalido += 1

        elif int(dados[2]) < 0:
            print('dado inconsistente. altitude negativa.')
            invalido += 1

print('{} dados válidos.'.format(validos))


