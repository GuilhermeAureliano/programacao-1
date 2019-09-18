# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

referencia = int(input())

soma = 0
for e in range(10):
    num = int(input())
    if num % referencia == 0:
        soma += num

print(soma)
