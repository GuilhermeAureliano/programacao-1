# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Perda de Tempo

soma = 0
for i in range(5): # dá pra fazer sem usar for, mas fiquei com preguiça de criar 5 variáveis
    perda = int(input())
    soma += perda

print('Você perdeu {} min na semana (média de {:.1f} min por dia).'.format(soma,(soma/5)))


produtiva = (soma * 100) / 7200
print('Isso significa {:.2f}% da sua semana produtiva.'.format(produtiva))

house = soma // 50
print('Daria para assistir {} episódio(s) de House.'.format(house))
