# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Digito Verificador de 5 Digitos

digito = input()

soma = 0
for i in range(len(digito)): # dá pra fazer sem usar o for
    soma += int(digito[i]) # transforma em inteiro cada digito na posição i
 
verificador = soma % 11

print('{}-{:02}'.format(digito, verificador))








