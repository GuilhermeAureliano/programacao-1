# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

n = int(input())

palavra = []
dobrada = []
n_dobrada = []

for i in range(n):
    palavra.append(input())

    ja_escrita = False
    duplicada = False
    pos = palavra[i] # posição

    for j in range(1,len(pos)):

        if pos[j] == pos[j-1] and not ja_escrita:
            dobrada.append(pos)

            duplicada = True
            ja_escrita= True

    if not duplicada:
        n_dobrada.append(pos)

dobr = len(dobrada)
sem_dobrada = len(n_dobrada)


print('{} palavra(s) com letras dobradas:'.format(dobr))
for i in range(dobr):
    print(dobrada[i])


print('---')
print('{} palavra(s) sem letras dobradas:'.format(sem_dobrada))

for i in range(sem_dobrada):
    print(n_dobrada[i])
