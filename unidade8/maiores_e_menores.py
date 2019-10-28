# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

pivot = int(input())
maiores, menores = [], []
while True:
    num = int(input())
    if num < 0: break
    if num <= pivot:
        menores.append(num)
    elif num > pivot:
        maiores.append(num)

print(menores)
print(pivot)
print(maiores)
