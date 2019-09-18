# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

tempo = int(input())

if tempo <= 3:
    preco = 1 + tempo * 0.5
    print('R$ {:.2f}'.format(preco))

else:
    i5 = tempo // 5
    resto = tempo % 5

    preco = 1 + i5 * 3 + resto * 0.7
    print('R$ {:.2f}'.format(preco))
