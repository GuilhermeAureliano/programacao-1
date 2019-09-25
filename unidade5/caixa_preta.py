# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

peso = comb = alti = 0
msg = ''

while True:
    dados = input().split()

    if int(dados[0]) < 0:
        msg = 'peso negativo.'
        break
    else:
        peso += 1
    if int(dados[1]) < 0:
        msg = 'combustível negativo.'
        break
    else:
        comb += 1
    if int(dados[2]) < 0:
        msg = 'altitude negativa.'
        break
    else:
        alti += 1

print('dado inconsistente. {}'.format(msg))
print('peso: {}'.format(peso))
print('combustível: {}'.format(comb))
print('altitude: {}'.format(alti))


