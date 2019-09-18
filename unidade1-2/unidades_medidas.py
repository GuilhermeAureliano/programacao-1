# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Unidades de Medidas

# 1 = 1,09361 jardas
# 1 = 3,28084 pés
# 1 = 39,3701 polegadas
metros = float(input())

jardas = metros * 1.09361
pés = metros * 3.28084
polegadas = (metros*100* 36) / 91.44

print('Jardas: {:.3f} yd'.format(jardas))
print('Pés: {:.3f} ft'.format(pés))
print('Polegadas: {:.3f} in'.format(polegadas))
