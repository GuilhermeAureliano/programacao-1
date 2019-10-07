# UFCG
# Programação 1 – 2019.2
# Guilherme Aureliano 

soma = cont = 0
lista = []

while True:
    n = input()
    
    if n == 'fim': break
    else:
        n = int(n)
        lista.append(n)
        soma += n
        cont += 1
print('%.2f' % (soma/cont))

i = 1
for e in lista:
    if e < (soma / cont):
        print(i,e)
    i += 1

