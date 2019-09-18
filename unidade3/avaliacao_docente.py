# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

semestres = int(input())
ensino = float(input())
intelectual = float(input())
orientacao = float(input())
admi = float(input())

if semestres >= 4:
    if ensino >= 320 and intelectual >= 100 and orientacao >= 20:
        media = (ensino + intelectual + orientacao + admi) / 4
        if media >= 140:
            print('Promoção deferida. Parabéns!')
        else:
            print('Promoção indeferida. Média insuficiente.')

    else:
        print('Promoção indeferida. Pontuação mínima não alcançada.')

else:
    print('Promoção indeferida. Número de semestres insuficiente.')
