# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

nomes, quant = [], []
soma = 0
while True:
    professor = input()
    if professor == '**': break
    else:
        nomes.append(professor)
        while True:
            questoes = input()
            if questoes == '*':
                quant.append(soma)
                soma = 0
                break
            else:
                soma += int(questoes)
print('Relatório de novas questões:\n')
total = 0
for i in range(len(nomes)):
    print('{}: {}'.format(nomes[i], quant[i]))
    total += quant[i]
print('---')
print('Total de novas questões: {}'.format(total))
