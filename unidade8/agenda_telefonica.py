# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

nomes, fone = [], []
letras = []
cont = 0

while True:
    entrada = input()
    if entrada == 'finalizar': break
    else:
        if entrada == '1' or entrada == 'inserir':
            n = int(input())
            for i in range(n):
                nomes.append(input())
                fone.append(input())
        elif entrada == '2' or entrada == 'buscar':
            encontrar = input()
            cont = False
            for i in range(len(nomes)):
                if nomes[i] == encontrar:
                    print('Nome: {}'.format(nomes[i]))
                    print('Fone: {}'.format(fone[i]))
                    print('----------')
                    cont = True
            if cont == False:
                print('Nome inexistente')
                print('----------')
        else:
            for i in range(len(nomes)):
                for j in range(len(nomes) - 1):
                    if nomes[j] > nomes[j + 1]:
                        nomes[j], nomes[j + 1] = nomes[j + 1], nomes[j]
                        fone[j], fone[j + 1] = fone[j+ 1], fone[j]
            for i in range(len(nomes)):
                print('Nome: {}'.format(nomes[i]))
                print('Fone: {}'.format(fone[i]))
                print('----------')
