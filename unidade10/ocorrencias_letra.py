# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def conta_letras(frase):
    letras = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
              'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'x': 0, 'w': 0, 'y': 0, 'z': 0}
    for e in frase:
        for k in letras.keys():
            if e == k:
                letras[k] += 1
    letra, cont = '', 0
    for k, v in letras.items():
        if cont < v:
            cont = v
            letra = k
    print('{} {}'.format(letra, cont))
frase = input().lower()
conta_letras(frase)

