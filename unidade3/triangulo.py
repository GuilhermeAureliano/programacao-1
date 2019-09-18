# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

a = float(input())
b = float(input())
c = float(input())

if (a - b < c < a + b) and (a - c < b < a + c ) and (b-c < a < b + c):
    print('triangulo valido. {:.0f}'.format(a + b + c))
else:
    print('triangulo invalido.')
