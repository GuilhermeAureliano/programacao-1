# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

n = int(input())
times = []
pontos = []
pos = []

for i in range(n):
    times.append(input())
    pontos.append(input())
    pos.append(i+1)

for i in range(1,n):
    if pontos[i] == ponto[i-1]:
        pos[i] = pos[i-1]

for i in range(n):
    print('{}. {} ({})'.format(pos[i], times[i], pontos[i]))
