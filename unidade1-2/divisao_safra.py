# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Divisão da Safra

soja = int(input())
atacado = int(input())
varejo = int(input())

A = soja // atacado
V = (soja - atacado * A)/varejo


print('Clientes no atacado = {}kg cada.'.format(A))
print('Clientes no varejo = {:.2f}kg cada.'.format(V))


