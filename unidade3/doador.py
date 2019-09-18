# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

aboP = input()
rhP = input()

aboD = input()
rhD = input()

if aboP == 'AB':
    if rhP == '-' and rhD == '-':
        print('compatível')
    elif rhP == '+':
        print('compatível')
    else:
        print('incompatível')

elif aboP == 'A':
    if aboD == 'A' or aboD == 'O':
        if rhP == '-' and rhD == '-':
            print('compatível')
        elif rhP == '+':
            print('compatível')
        else:
            print('incompatível')
    else:
        print('incompatível')

elif aboP == 'B':
    if aboD == 'B' or aboD == 'O':
        if rhP == '-' and rhD == '-':
            print('compatível')
        elif rhP == '+':
            print('compatível')
        else: 
            print('incompatível')
    else:
        print('incompatível')

else:
    if aboP == aboD:
        if rhP == '-' and rhD == '-':
            print('compatível')
        elif rhP == '+':
            print('compatível')
        else:
            print('incompatível')
    else:
        print('incompatível')








