# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

cre = float(input())
meses = int(input())
entrevista = float(input())

if cre < 7 and meses < 6:
    print('Candidato eliminado. CRE e experiência abaixo do limite.')
elif cre < 7 and meses >= 6:
    print('Candidato eliminado. CRE abaixo do limite.')
elif cre >= 7 and meses < 6:
    print('Candidato eliminado. Experiência abaixo do limite.')

else:
    if entrevista <= 3:
        print('Candidato classificado.')
    else:
        print('Candidato aprovado.')
