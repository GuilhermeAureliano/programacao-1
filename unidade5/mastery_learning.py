# UFCG
# Programação 1 – 2019.2
# Guilherme Aureliano 

print('Mastery Learning\nCálculo da nota na unidade\n')

cont = soma = 0
lista = []
pen = 0

while True:
    if cont == 0:
        nota = float(input('Nota? '))
        lista.append(nota)
        cont += 1
        soma += nota
    else:
        cont += 1
        nota = float(input('Nota? '))
        if cont > 2:
            pen += 1
        lista.append(nota)
        for i in range(len(lista)): # BubbleSort para ordenar os valores da lista do menor ao maior
            for j in range(len(lista) - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        media = (lista[-1] + lista[-2]) / 2
        if media >= 6.5:
            msg = 'aprovado'
        else:
            msg = 'cursando'
        print('Média: {:.1f} ({})'.format(media, msg))
        print('Penalização: {:.1f}'.format(pen * 0.5))
        print()
        if msg == 'aprovado':
            print('===')
            print('Notas válidas: {:.1f} e {:.1f}'.format(lista[-1], lista[-2]))
            print('Média parcial na unidade: {}'.format(media))
            print('Penalizações: {:.1f}'.format(pen * 0.5))
            print('Média final na unidade: {:.1f}'.format(media - (pen*0.5)))
            break

