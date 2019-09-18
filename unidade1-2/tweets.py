# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Tweets

tweets = int(input())
paginas = tweets // 400

print('Serão necessárias {} página(s) para visualizar os tweets.'.format(paginas))

if tweets >= 400:
    perdidos = tweets - (400 * paginas)
    print('{:.1f}% dos tweets serão perdidos.'.format((perdidos * 100)/tweets))
else:
    perdidos = 100
    print('{:.1f}% dos tweets serão perdidos.'.format(perdidos))





