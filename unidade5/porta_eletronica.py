registro = []
while True:
    codigo = input().split()
    if codigo[0] == 'S':
        break

    if codigo[0] == 'R':
        for i in range(len(codigo)):
            registro.append(codigo[1][0])
            break
    elif codigo[0] == 'P':
        cont = 0
        for i in range(len(registro)):
            if registro[i] == codigo[1][0]:
                cont += 1
        print(cont)
            
            
