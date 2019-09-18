# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aurelian

entrada = input()
pares = ''

for i in range(len(entrada)):
    if i % 2 == 0:
        pares += entrada[i]

print(pares)
