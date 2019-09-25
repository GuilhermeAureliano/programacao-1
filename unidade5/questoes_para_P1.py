# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

nomes = []
cont = []
soma = 0
parametro = False
while True:
    if parametro == False:
        professor = input()
    if professor == '**':
        break
    else:
        num = input()
        if num == '*':
            cont.append(soma)
            soma = 0
            parametro = False
            if professor == '**':
                break
            else:
                nomes.append(professor)
        else:
            parametro = True
            soma += int(num)
print('Relatório de novas questões:')
print()
saida = ''
for i in range(len(nomes)): # For para concatenar strings
    if i == len(nomes) - 1:
        saida += nomes[i]+':'+' '+str(cont[i])
    else:
        saida += nomes[i] + ':'+' '+str(cont[i]) + '\n'
if saida != '':
    print(saida)
print('---')
total = 0
for i in range(len(cont)):
    total += cont[i]
print('Total de novas questões: {}'.format(total))
