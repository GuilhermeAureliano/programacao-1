# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

N = int(input())
lista = []
menor = 999999999 # maior número possível (infinito)
maior = 0

for i in range(N):
	num = int(input())
	lista.append(num)
	if menor > num:
		menor = num
	if maior < num:
		maior = num

acm =  abx = 0

extremos = (maior +  menor) / 2

for i in range(len(lista)):
	if lista[i] >= 0:
		if lista[i] > extremos:
			acm += 1
		else:
			abx += 1

print('Menor número:',menor)
print('Maior número:',maior)
print('Média dos extremos:','%.2f' % (extremos))
print('{} número(s) abaixo da média'.format(abx))
print('{} número(s) acima da média'.format(acm))
