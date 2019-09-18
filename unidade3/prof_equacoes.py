# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

a = int(input())
b = int(input())
c = int(input())

delta = b ** 2 - 4 * a * c

if delta == 0:
    x1 = (-(b) + delta ** 0.5) / ( 2 * a )
    print('x = {:.2f}'.format(x1))

elif delta < 0:
    print('sem raizes reais')

else:
    x1 = (-(b) + delta ** 0.5) / ( 2 * a )
    x2 = (-(b) - delta ** 0.5) / (2 * a )
    print('x1 = {:.2f}'.format(x1))
    print('x2 = {:.2f}'.format(x2))

