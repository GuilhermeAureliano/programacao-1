# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Conversão para Graus Decimais

graus = float(input())
minutos = float(input())
segundos = float(input())

graus_decimais = graus + (( minutos / 60) + (segundos/3600))

print('graus = {:.4f}'.format(graus_decimais))
