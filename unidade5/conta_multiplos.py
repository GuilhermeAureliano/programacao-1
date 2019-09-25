# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

K = int(input())

casos = 0
while True:
    entrada = input().split()
    if entrada[0] == 'fim':
        break
    
    if int(entrada[0]) % K == 0 and int(entrada[1]) % K == 0:
        casos += 1

print(casos)
