# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

palavra = input()

trocas = 0
convertida = ''


for i in range(len(palavra)):
    if i != 0:
        if palavra[i] == 'a' or palavra[i] == 'A':
            convertida += '4'
            trocas += 1
    
        elif palavra[i] == 'e' or palavra[i] == 'E':
            convertida += '3'
            trocas += 1

        elif palavra[i] == 'i' or palavra[i] == 'I':
            convertida += '1'
            trocas += 1

        elif palavra[i] == 'o' or palavra[i] == 'O':
            convertida += '0'
            trocas += 1

        else:
            convertida += palavra[i]
    else:
        convertida += palavra[i]

print('{} ({} troca(s))'.format(convertida, trocas))
