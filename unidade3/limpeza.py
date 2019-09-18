# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

servico = int(input())
if servico != 3:
    tamanho = float(input())

if servico == 1 or servico == 2:
     if servico == 1:
         preco = 80 * tamanho
         print('R$ {:.0f},00'.format(preco))
         if preco >= 200:
             print('Brinde!')
     else:
         preco = 50 * tamanho
         print('R$ {:.0f},00'.format(preco))
         if preco >= 200:
             print('Brinde!')

else:
    print("R$ 50,00")
