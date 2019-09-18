# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

palavra = input()
fonte = input()

nova = ''
cont = -1

for e in range(len(palavra)):
    nova += str(int(fonte[cont]) * palavra[e] + palavra[e])
    cont -= 1

print(nova)
