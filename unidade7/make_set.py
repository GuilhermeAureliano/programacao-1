def verify(lista, termo):
    possui = False
    for e in lista:
        if e == termo:
            possui = True
    return possui

def teste(lista):
    lista_aux = []
    for e in lista:
        print(e, lista_aux)
        if not verify(lista_aux, e):
            lista_aux.append(e)

def make_set(lista):
    lista_aux = []
    i = 0
    while True:
        if i >= len(lista): break
        if not verify(lista_aux, lista[i]):
            lista_aux.append(lista[i])
            i += 1
        else:
            lista.pop(i)
            lista_aux = []
            i = 0


