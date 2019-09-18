# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Calcula Hipotenusa

cateto1 = float(input('Medida do Cateto 1? '))
cateto2 = float(input('Medida do Cateto 2? '))

hipotenusa = (cateto1 **2 + cateto2 **2)**(1/2)

print('Medida da Hipotenusa: {}'.format('%.2f' % hipotenusa))


