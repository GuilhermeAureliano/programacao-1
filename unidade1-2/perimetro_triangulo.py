# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Perimetro Triângulo

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

# Distância de A até B
dAB = (x2 - x1) ** 2 + (y2 - y1) ** 2
raizAB = dAB ** (1/2)

# Distância de B até C
dBC = (x3 - x2) ** 2 + (y3 - y2) ** 2
raizBC = dBC ** (1/2)

# Distância de C até A
dCA = (x3 - x1) ** 2 + (y3 - y1) ** 2
raizCA = dCA ** (1/2)

perimetro = raizAB + raizBC + raizCA 
print('O perímetro é de {:.2f}'.format(perimetro))

