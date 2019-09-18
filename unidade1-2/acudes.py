# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Açudes

c = float(input('capacidade? '))
p = float(input('percentual hoje? '))
g = float(input('gasto diário? '))

v = (p * c) / 100
restantes = v // g

print('volume: {:.2f}'.format(v))
print('dias restantes: {:.0f}'.format(restantes))
