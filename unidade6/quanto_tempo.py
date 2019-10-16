# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def quanto_tempo(horario1, horario2):
    for i in range(len(horario1)):
        h1 = horario1.split(':')
        for inteiro in range(len(h1)):
            h1[inteiro] = int(h1[inteiro])
    for i in range(len(horario2)):
        h2 = horario2.split(':')
        for inteiro in range(len(h2)):
            h2[inteiro] = int(h2[inteiro])
    horas = h2[0] - h1[0]
    minutos = h2[1] - h1[1]
    if minutos < 0:
        horas -= 1
        minutos += 60
    msg = '{} hora(s) e {} minuto(s)'.format(horas, minutos)
    return msg
