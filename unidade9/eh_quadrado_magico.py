# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def eh_quadrado_magico(quadrado):
    if len(quadrado) != len(quadrado[0]): return False
    linha, coluna = 0, 0
    elementos = []
    referencia, cont = 0, 0
    for i in range(len(quadrado)):
        s1, s2 = 0, 0
        for j in range(len(quadrado[0])):
            elementos.append(quadrado[i][j])
            if cont == 0:
                referencia += quadrado[i][j]
            s1 += quadrado[i][j]
            s2 += quadrado[j][i]
        cont += 1
        if s1 == s2:
            linha += 1
            coluna += 1
    print(referencia)
    for i in range(len(elementos)):
        for j in range(1, len(elementos)):
            if i != j and elementos[i] == elementos[j]: return False
    if linha == len(quadrado[0]) and coluna == len(quadrado[0]):
        ds, dp = 0, 0
        for i in range(len(quadrado)):
            for j in range(len(quadrado[0])):
                if i == j:
                    dp += quadrado[i][j]
                if i + j == len(quadrado) - 1:
                    ds += quadrado[i][j]
        if ds == referencia and dp == referencia:
            return True
        else:
            return False
    else:
        return False

