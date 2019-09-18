# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

palavra = input()

inversa = ''
for i in range(len(palavra) -1, -1, -1):
    inversa += palavra[i]

iguais = 0
for i in range(len(palavra)):
    if inversa[i] == palavra[i]:
        iguais += 1

print('A palavra {} contém {} caractere(s) coincidente(s) com a sua inversa.'.format(palavra, iguais))

