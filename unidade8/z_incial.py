# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def z_inicial(lista):
    cont = 0
    for i in range(len(lista)):
        if lista[i][0] == 'z' or lista[i][0] == 'Z':
            cont += 1
    return cont
lista = input().split()
z_inicial(lista)
print(z_inicial(lista))
