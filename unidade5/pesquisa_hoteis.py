# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

tamanho = conforto = 0
valor = float('inf')
p1, p2, p3, letras = [], [], [], []
v1, v2, v3 = '', '', ''

while True:
    entrada = input().split(',')
    if entrada[0] == '---':
        for i in range(len(letras)):
            if valor > p1[i]:
                valor = p1[i]
                v1 = letras[i]
            if tamanho < p2[i]:
                tamanho = p2[i]
                v2 = letras[i]
            if conforto < p3[i]:
                conforto = p3[i]
                v3 = letras[i]
        break
    else:
        p1.append(float(entrada[0]))
        p2.append(float(entrada[1]))
        p3.append(float(entrada[2]))
        letras.append(entrada[-1])

while True:
    pesquisa = input()
    if pesquisa == 'fim': break
    if pesquisa == 'valor':
        print(v1)
    elif pesquisa == 'tamanho':
        print(v2)
    else:
        print(v3)
