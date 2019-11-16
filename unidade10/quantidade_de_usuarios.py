# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def quantidade_usuarios(cadastro):
	cont = 0
	for k, v in cadastro.items():
		if k != 9999:
			cont += len(v)
	return cont
