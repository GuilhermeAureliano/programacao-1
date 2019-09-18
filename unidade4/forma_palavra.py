# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

palavra = []
for e in range(3):
    palavra.append(input())

l1 = palavra[0]
l2 = palavra[1]
l3 = palavra[2]

new = ''
for i in range(len(l1)): # serve para qualquer tamanho
    if l1[i] > l2[i] and l1[i] > l3[i]:
        new += l1[i]
    elif l2[i] > l1[i] and l2[i] > l3[i]:
        new += l2[i]
    else:
        new += l3[i]

print(new)
