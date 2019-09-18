# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Área do Cilindro

import math

print('Cálculo da Superfície de um Cilindro')
print('---')

diametro = float(input('Medida do diâmetro? '))
altura = float(input('Medida da altura? '))
print('---')

raio = diametro / 2
al = 2 * math.pi * raio * altura
ab = math.pi * raio ** 2
total = al +2 * ab 

print('Área calculada: {:.2f}'.format(total))


