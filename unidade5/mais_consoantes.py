# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

vogais = 'aeiou'
lidas = 0

while True:
    entrada = input().lower()
    lidas += 1

    cont = 0
    for i in range(len(entrada)):
        if entrada[i] in vogais:
            cont += 1
    
    dif = len(entrada) - cont
    if cont < dif:
        break
print(lidas)
