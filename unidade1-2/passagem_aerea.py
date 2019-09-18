# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Passagem Áerea

d1 = float(input())
d2 = float(input())

valor = d1 * d2 + 51
print('Valor da passagem: R$ {:.2f}'.format(valor))
print()
print('Pagamento:')

avista = valor * 0.75
six = valor * 0.95

print('1. À vista. R$ {:.2f}'.format(avista))

# a função sep separa as string pelo que está dentro das aspas
print('2. Em 6 parcelas. Total: R$ {:.2f}'.format(six))
print('','6 x R$ {:.2f}'.format(six/6), sep= '   ')

print('3. Em 10 parcelas. Total: R$ {:.2f}'.format(valor))
print('','10 x R$ {:.2f}'.format(valor/10), sep = '   ')
