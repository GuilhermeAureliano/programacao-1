# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Espaço em Disco Simplificado

um = input()
byte1 = float(input())

dois= input()
byte2 = float(input())

tres = input()
byte3 = float(input())

print('SPLab - Espaço utilizado pelos usuários')
print('---------------------------------------------')
print('Nr., Usuário, Espaço Utilizado')
print()

MB1 = (byte1/1024)/1024
MB2 = (byte2/1024)/1024
MB3 = (byte3/1024)/1024

print('1, {}, {:.2f} MB'.format(um, MB1))
print('2, {}, {:.2f} MB'.format(dois, MB2))
print('3, {}, {:.2f} MB'.format(tres, MB3))
print()

print('Espaço total ocupado: {:.2f} MB'.format(MB1 + MB2 + MB3))
print('Espaço médio ocupado: {:.2f} MB'.format((MB1 + MB2+MB3) / 3 ))
