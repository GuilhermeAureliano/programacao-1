# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

idade = int(input('Idade? '))

if idade < 12:
    print('criança (meia entrada)')
elif idade >= 65:
    print('idoso (meia entrada)')
else:
    estudante = input('Estudante? ')
    if estudante == 'n':
        print('adulto (inteira)')
    else:
        publica = input('Rede Pública? ')
        if publica == 'n':
            print('estudante (meia entrada)')
        else:
            print('estudante da rede pública (isento)')

