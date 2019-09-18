# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

meses = ['jan','fev','mar','abr','mai','jun','jul',
        'ago','set','out','nov','dez']
cont = 0
lucro = 0

for i in range(12):
    mes = input().split()

    lucro = float(mes[0]) - float(mes[1])
    if lucro < 0:
        print('{} {:.1f}'.format(meses[cont], lucro))
        cont += 1

    else:
        print('{}  {:.1f}'.format(meses[cont], lucro))
        cont += 1

