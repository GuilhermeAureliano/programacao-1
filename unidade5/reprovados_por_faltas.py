# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

rep = 0

while True:
    faltas = input()

    if faltas == '-':
        break

    cont = 0
    i = 0
    while i <= len(faltas) - 1:
        if faltas[i] == 'f':
            cont += 1
        i += 1
        if cont > 8:
            break

    if cont > 8:
        rep += 1

print('{} aluno(s) reprovado(s) por falta.'.format(rep))
