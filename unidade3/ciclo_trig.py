# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

posicao = float(input())
if posicao > 360:
    newposicao = posicao - 360 * (posicao // 360)
else:
    newposicao = posicao

if 90 >= newposicao >=  0:
    if newposicao == 90:
        print('Sobre eixos')
    elif newposicao == 0:
        print('Sobre eixos')
    else:
        print('Quadrante 1')

elif 90 < newposicao <= 180:
    if newposicao == 180:
        print('Sobre eixos')
    else:
        print('Quadrante 2')

elif 180 < newposicao <= 270:
    if newposicao == 270:
        print('Sobre eixos')
    else:
        print('Quadrante 3')
else:
    if newposicao == 360:
        print('Sobre eixos')
    else:
        print('Quadrante 4')
