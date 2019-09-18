# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

area = float(input())
valor = float(input())
pagamento = input()

preco = area * valor

if pagamento == 'vista':
    print('Total: R$ {:.2f}'.format(preco*0.8))
elif pagamento == '2x':
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(preco*0.9,(preco*0.9)/2))
else:
    print('Total: R$ {:.2f}. Parcelas: R$ {:.2f}'.format(preco*0.95, (preco*0.95)/3))

