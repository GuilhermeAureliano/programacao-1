lim = int(input())
base = 2
expoente = 0
soma = 0
lista = []
cont = 0

while True:
    x = base ** expoente
    expoente += 1
    soma += x
    lista.append(x)
    if soma < lim:
        saida = ''
        for i in range(len(lista)):
            if i == len(lista) - 1:
                saida += str(lista[i])
                cont += 1
            else:
                cont += 1
                saida += str(lista[i]) + '\n'
    else:
        if cont >= 1:
            print(saida)
        break
