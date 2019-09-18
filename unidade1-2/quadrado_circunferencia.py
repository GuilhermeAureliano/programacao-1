# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Quadrado na Circunferência

import math

lado = float(input())

raio = (lado * 2 ** 0.5) / 2
per = 2 * math.pi * raio
area = math.pi * raio ** 2

print('Perímetro: {:.5f}'.format(per))
print('Área: {:.5f}'.format(area))


