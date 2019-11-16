# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def ausentes(livros):
	estoques = 0
	for v in livros.values():
		if v == 0:
			estoques += 1
	return estoques
