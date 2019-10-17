# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def maior_palavra(frase):
    frase = frase + str('  ')
    maior, palavra = '', ''
    for e in frase:
        if e != ' ':
            palavra += e
        elif palavra != '':
            if len(palavra) >= len(maior):
                maior = palavra
            palavra = ''
    return maior
