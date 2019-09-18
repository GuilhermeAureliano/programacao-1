# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aurelian

N = int(input())

inteiros = input().split()
encontrou = False

for i in range(len(inteiros)):
    if str(N) == inteiros[i]:
        encontrou = True

if encontrou == True:
    print('sim')
else:
    print('não')
