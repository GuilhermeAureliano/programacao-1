# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

numero = input()
elementos = input().split()

posicoes = ''
for i in range(len(elementos)):
    if i < len(elementos):
        if numero == elementos[i]:
            posicoes += str(i) + ' '
if len(posicoes) == 0:
    print(-1)

else:
    print(posicoes[:-1]) # É proibido usar slice [:-1], porém eu não estava conseguindo fazer sem!

        


