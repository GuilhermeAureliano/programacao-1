# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

n = 1

vogais = 'aeiouAEIOU'
contvogais = 0
chave = input()

for letra in chave:
  if contvogais <= 5:
    if letra in vogais:
        contvogais += 1
    if letra + letra + letra in chave:
        print('Chave insegura. 3 caracteres consecutivos iguais.')
        n = 0
        break
  else:
	  print('Chave insegura. 6 vogais.')
	  n = 0
	  break
if n == 1:
    print('Chave segura!')
