# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Consumo de Energia

potencia = float(input())
minutos = float(input())

horas = minutos / 60

consumo_kwh = (potencia * horas)/1000

print('%.1f' % consumo_kwh,'kWh')
