# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Calcula Moldura

comprimento = float(input())
largura = float(input())

preco = ((comprimento/100 * 2) + (largura/100 * 2)) * 120

print('R$ {:.1f}'.format(preco))
