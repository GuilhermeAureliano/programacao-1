# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

altura = int(input())

largura = 1
espacos = altura - 1

for arvore in range(altura):
	print (espacos * " " + "o" * largura)
	largura += 2
	espacos -= 1

print ((altura - 1) * " " + "o")

# Confesso que não fiz esse código!

