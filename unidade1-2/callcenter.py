# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Callcenter

soma = 0
for i in range(7):  # Usei for porque eu estava com preguiça de escrever 7 linhas
    atendimentos = int(input())
    soma += atendimentos

print('Total: {}'.format(soma))
print('Média: {:.2f}'.format((soma/7)))
