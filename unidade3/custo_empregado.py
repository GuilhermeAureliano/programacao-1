# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

bruto = float(input())
dias = int(input())
transporte = float(input())

empregador = 0
desconto = 0
liquido = 0

if bruto <= 1317.07:
    desconto = 0.08 * bruto

elif 1317.08 <= bruto <= 2195.12:
    desconto = 0.09 * bruto
else:
    desconto = 0.11 * bruto

if dias * transporte > 0.06 * bruto:
    empregador = bruto * 0.12 + bruto * 0.08 + bruto + (dias * transporte - bruto * 0.06)
    liquido = bruto - desconto - (bruto * 0.06)
else:
    empregador = bruto * 0.12 + bruto * 0.08 + bruto
    liquido = bruto - desconto - (dias * transporte)


print('salário bruto = R$ {:.2f}'.format(bruto))
print('custo mensal = R$ {:.2f}'.format(empregador))
print('salário líquido = R$ {:.2f}'.format(liquido))

