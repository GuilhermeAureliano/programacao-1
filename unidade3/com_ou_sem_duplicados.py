# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

um = float(input())
dois = float(input())
tres = float(input())
quarto = float(input())
cinco = float(input())

cont = 0
if um == dois or um == tres or um == quarto or um == cinco:
    cont += 1
if dois ==  tres or dois == quarto or dois == cinco:
    cont += 1
if tres == quarto or tres == cinco:
    cont += 1
if quarto == cinco:
    cont += 1

if cont >= 1:
    print('com duplicados')
else:
    print('sem duplicados')
