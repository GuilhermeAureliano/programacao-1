# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Movimento Uniformemente Variado

# v = v0 + a * t
# s = s0 + v0 * t + (a*t**2)/2

s0 = float(input('Posição inicial? '))
v0 = float(input('Velocidade inicial? '))
t = float(input('Tempo? '))
a = float(input('Aceleração? '))
print()
print('Dados da questão')
print('================')

# sep = '' ----> serve para separar duas string pelo que está dentro das aspas
print('','Posição inicial: {:.2f} m'.format(s0),sep = '   ')
print('Velocidade inicial: {:.2f} m/s'.format(v0))
print('','Aceleração: {:.2f} m/s2'.format(a),sep ='        ')
print('','Tempo: {:.2f} s'.format(t),sep = '             ')

v = v0 + a * t
print('','Velocidade final: {:.2f} m/s'.format(v), sep = '  ')

vm = v0 + (a*t)/2
print('','Velocidade média: {:.2f} m/s'.format(vm), sep= '  ')

s = s0 + v0 * t + (a*t**2)/2
print('','Posição final: {:.2f} m'.format(s), sep= '     ')


