# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def adiciona_item(item, lista):
    indices = []
    itens = []
    for i in range(len(lista)):
        e = lista[i]
        if item < e:
            itens.append(e)
            indices.append(i)
    cont = 0        
    for i in indices:
        lista.pop(i - cont)
        cont += 1
    lista.append(item)
    for e in itens:
        lista.append(e)
    return lista

