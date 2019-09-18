# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Reajuste

atual = float(input("Valor atual? "))
novo = float(input("Novo valor? "))

reajuste = novo - atual
x = (reajuste*100)/atual

print("Reajuste de {:.1f}%".format(x))

