# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# IMC

peso = float(input())
altura = float(input())

IMC = peso / (altura ** 2 )
x = (altura ** 2) * 24.9
ideal = x - peso

print('IMC atual = {:.2f}'.format(IMC))
print('Peso a ser ganho/perdido = {:.2f}'.format(ideal))
