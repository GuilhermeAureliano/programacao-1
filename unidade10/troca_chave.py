# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def troca_chave(dic):
	inverso = {}
	for k, v in dic.items():
		inverso[v] = k
	return inverso
