# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

um = input().split()
dois = input().split()

somaUm = 0

for i in range(len(um)):
    somaUm += float(um[i])

mediaUm = somaUm / len(um)

x1 = df1 = 0
for i in range(len(um)):
    df1 = (float(um[i]) - mediaUm) ** 2
    x1 += df1
    df1 = 0

desvioUm = '%.2f' %  (( x1 / (len(um) - 1)) ** 0.5)

somaDois = 0

for i in range(len(dois)):
    somaDois += float(dois[i])

mediaDois = somaDois / len(dois)

x2 = df2 = 0
for i in range(len(dois)):
    df2 = (float(dois[i]) - mediaDois) ** 2
    x2 += df2
    df2 = 0

desvioDois = '%.2f' % (( x2 / (len(dois) - 1)) ** 0.5)

if desvioUm > desvioDois:
    print('A sequência {} possui o maior desvio padrão ({}).'.format(1, desvioUm))
elif desvioUm < desvioDois:
    print('A sequência {} possui o maior desvio padrão ({}).'.format(2, desvioDois))
else:
    print('As sequências possuem o mesmo desvio padrão ({}).'.format(desvioUm))

