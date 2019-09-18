# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

n11 = float(input())
n21 = float(input())
n31 = float(input())
idade1 = int(input())

n12 = float(input())
n22 = float(input())
n32 = float(input())
idade2 = int(input())

candidato1 = ( n11 * 0.3  + n21 * 0.4  + n31 * 0.3) / 1
candidato2 = ( n12 * 0.3  + n22 * 0.4 + n32 * 0.3 ) / 1

if candidato1 > candidato2:
    print('O primeiro candidato foi aprovado com média {:.1f}.'.format(candidato1))

elif candidato1 < candidato2:
    print('O segundo candidato foi aprovado com média {:.1f}.'.format(candidato2))

else:
    if idade1 > idade2:
        print('O primeiro candidato foi aprovado com média {:.1f}.'.format(candidato1))
    elif idade1 < idade2:
         print('O segundo candidato foi aprovado com média {:.1f}.'.format(candidato2))
    else:
        print('Empate.')

