# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# CNPJ

entrada = input()
numeros = '0123456789'

soma = 0
for i in range(len(entrada)): # dá pra fazer sem usar o for
    if entrada[i] in numeros: # significa que é um número e não um ponto
        soma += int(entrada[i])

print('{}/0001-{:02}'.format(entrada, soma + 1))
