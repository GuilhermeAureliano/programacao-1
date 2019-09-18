# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Morangos

morangos = int(input())
caixas = morangos // 400

print('Serão necessárias {} caixa(s) para embalar os morangos.'.format(caixas))

if morangos >= 400:
    perdidos = morangos - (400 * caixas)
    print('{:.1f}% dos morangos serão perdidos.'.format((perdidos * 100)/morangos))
else:
    perdidos = 100
    print('{:.1f}% dos morangos serão perdidos.'.format(perdidos))
