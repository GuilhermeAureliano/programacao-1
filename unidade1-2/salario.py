# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Salário

salario_bruto = float(input())
horas_de_trabalho = float(input())

hora_bruta = salario_bruto / horas_de_trabalho

print('Salário Bruto = {}'.format('%.2f' % salario_bruto))

print('Hora Bruta = {}'.format('%.2f' % hora_bruta))

print('Desconto IR = {}'.format('%.2f' % (salario_bruto * 0.11)))

print('Desconto INSS = {}'.format('%.2f' % (salario_bruto * 0.08)))

print('Desconto Sindicato = {}'.format('%.2f' % (salario_bruto * 0.05)))

hora_liquida = (salario_bruto - (salario_bruto * 0.11) -(salario_bruto * 0.08) - (salario_bruto * 0.05)) / horas_de_trabalho
liquida = salario_bruto -( salario_bruto * 0.11) -(salario_bruto * 0.08) - (salario_bruto * 0.05)

print('Salário Líquido = {}'.format('%.2f' % liquida))
print('Hora Líquida = {}'.format('%.2f' % hora_liquida))





