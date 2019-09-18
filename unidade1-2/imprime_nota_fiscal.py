# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Imprime Nota Fiscal

total = float(input())
data = input()
quantidade = int(input())

media = total/quantidade

print('Data: {}'.format(data))
print('O valor total da compra foi de R$ {:.2f}. A média do preço dos produtos é de {:.1f}.'.format(total, media))

