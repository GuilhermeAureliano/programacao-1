# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

antes = float(input())
depois = float(input())

gelo = (depois * 100) / antes
qualidade  = 100 - gelo

if 5 <=  qualidade < 10:
    print('{:.1f}% do peso do produto é de água congelada.'.format(qualidade))
    print('Produto em conformidade.')

elif qualidade < 5:
    print('{:.1f}% do peso do produto é de água congelada.'.format(qualidade))
    print('Produto qualis A.')

else:
    print('{:.1f}% do peso do produto é de água congelada.'.format(qualidade))
    print('Produto não conforme.')

    

