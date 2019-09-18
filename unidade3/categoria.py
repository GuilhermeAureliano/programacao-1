# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

# Infantil A - 5 a 7 anos
# Infantil B - 8 a 10 anos
# Juvenil A - 11 a 13 anos
# Juvenil B - 14 a 17 anos
# Senior - Acima de 17 anos
nome = input()
idade = int(input())

if 5 <= idade <= 7:    
    print('{}, {} anos, Infantil A.'.format(nome, idade))
elif 8 <= idade <= 10:
    print('{}, {} anos, Infantil B.'.format(nome, idade))
elif 11 <= idade <= 13:
    print('{}, {} anos, Juvenil A.'.format(nome, idade))
elif 14 <= idade <= 17:
    print('{}, {} anos, Juvenil B.'.format(nome, idade))
elif idade > 17:
    print('{}, {} anos, Senior.'.format(nome, idade))
else:
    print('{}, {} anos, Não pode competir.'.format(nome, idade))





