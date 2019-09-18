# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Votação

abstencao = int(input())
a_favor = int(input())
contra = int(input())

print('Resultado da Votação')
print()

total = abstencao + a_favor + contra

print('{} abstenções ({}%)'.format(abstencao, '%.2f' % ((abstencao * 100)/total)))
print('{} a favor ({}%)'.format(a_favor, '%.2f' % ((a_favor * 100)/total)))
print('{} contra ({}%)'.format(contra, '%.2f' % ((contra * 100 )/total)))

