# UFCG
# Programação 1 – 2019.2
# Guilherme Aureliano 

print('Mastery Learning\nCálculo da nota na unidade\n')

cont = 0
pen = 0 # Penalização
mudou = False # Variável de controle

n1 = n2 = 0 # Nota 1 e Nota 2
while True:
    if cont == 0:
        nota = float(input('Nota? '))
        n1 = nota
        cont += 1
    else:
        cont += 1
        nota = float(input('Nota? '))
        if cont == 2:
            n2 = nota
        if cont > 2:
            pen += 1
            if n1 < nota and n1 <= n2: # Verifica se a nova nota lida é maior que nota 1
                n1 = nota
                mudou = True
            if n2 < nota and n2 <= n1 and mudou == False: # Verifica se a nova nota lida é maior que nota 2
                n2 = nota
        media = (n1 + n2) / 2
        if media >= 6.5:
            msg = 'aprovado'
        else:
            msg = 'cursando'
        print('Média: {:.1f} ({})'.format(media, msg))
        print('Penalização: {:.1f}'.format(pen * 0.5))
        print()
        if msg == 'aprovado':
            print('===')
            print('Notas válidas: {:.1f} e {:.1f}'.format(n1, n2))
            print('Média parcial na unidade: {}'.format(media))
            print('Penalizações: {:.1f}'.format(pen * 0.5))
            print('Média final na unidade: {:.1f}'.format(media - (pen*0.5)))
            break
