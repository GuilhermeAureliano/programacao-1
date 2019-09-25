# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

while True:
    bcd = input()
    if bcd == 'fim':
        break
    if len(bcd) == 8:
        tabela = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001']
        cont = 0
        primeiro = ''
        segundo = ''
        for i in range(len(tabela)):
            if tabela[i] == bcd[0] + bcd[1] + bcd[2] + bcd[3]: # Os 4 primeiros digitos
                primeiro = str(i)
                cont += 1
            if tabela[i] == bcd[4] + bcd[5] + bcd[6] + bcd[7]: # Os 4 últimos digitos
                segundo = str(i)
                cont += 1
        if cont >= 2:
            print(primeiro+segundo) # número obtido

        else:
            print("BCD inválido.")
    else:
        print("Tente novamente.")

