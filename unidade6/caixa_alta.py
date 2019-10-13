# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def caixa_alta(frase):
    new = ''
    if len(frase) == 1:
        new += frase.lower()
    else: 
        for i in range(len(frase) - 1):
            if i == 0 and frase[i + 1] != ' ':
                new += frase[i].upper()
            elif i == 0 and frase[i + 1] == ' ':
                if frase[i] == frase[i].upper():
                    new += frase[i].lower()
                else:
                    new += frase[i]
            else:
                if frase[i + 1] == ' ' and frase[i - 1] == ' ':
                        new += frase[i].lower()
                else:
                    if frase[i] != ' ' and frase[i -1] == ' ':
                        new += frase[i].upper()
                    else:
                        new += frase[i]

        new += frase[-1].lower()
    return new

