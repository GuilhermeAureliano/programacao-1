# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

pares = 0
impares = 0
mp = 0
mi = 0

for i in range(int(input())):
    num = int(input())

    if num % 2 == 0:
        pares += 1
        mp += num
    else:
        impares += 1
        mi += num

print('pares: {}'.format(pares))
print('ímpares: {}'.format(impares))
print('média pares: {:.1f}'.format(mp/pares))
print('média ímpares: {:.1f}'.format(mi/impares))
