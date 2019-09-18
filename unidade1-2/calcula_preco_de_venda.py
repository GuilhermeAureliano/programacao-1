# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Calcula preço de venda

custo = float(input())
despesas = float(input())
lucro = float(input())
impostos = float(input())
comissoes = float(input())
descontos = float(input())
encargos = float(input())

x = custo * despesas / 100
y = custo * lucro / 100

venda = (custo + x + y) * 100 / (100 - impostos - comissoes - descontos - encargos)

print('Preço de venda é R$ {:.2f} (R$ {:.2f} + R$ {:.2f})'.format(venda, int(venda), venda - int(venda)))

