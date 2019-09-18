# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

salario = float(input())

print('O valor da contribuição do INSS a ser pago pelo empregador é de R$ {:.2f}'.format(salario * 0.12))

if salario <= 1317.07:
    desconto = salario * 0.08
elif 1317.08 <= salario <= 2195.12:
    desconto = salario * 0.09
else:
    desconto = salario * 0.11

print('O valor da contribuição do INSS a ser pago pelo empregado é de R$ {:.2f}'.format(desconto))
