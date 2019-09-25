# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

cont = 0
soma = 0
media = 0

while True:
    investimento = float(input())
    if investimento < media:
        break
    soma += investimento
    cont += 1
    media = soma / cont

print('Saldo total do FIS: R${:.2f}.'.format(soma))
print('Média das contribuições: R${:.2f}.'.format(media))


