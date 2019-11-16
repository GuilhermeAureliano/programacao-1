# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def eh_roteiro(iata, voos, roteiro):
	def In(lista, elemento):
		for e in lista:
			if e==elemento:return True
		return False
	roteiro=[e for e in roteiro.split('/')]
	for i in range(len(roteiro)):
		roteiro[i] = iata[roteiro[i]]
	for k,v in voos.items():
		chave = k
		aeroporto = v
		if chave==roteiro[0]:
			for i in range(1,len(roteiro)):
				if not In(aeroporto, roteiro[i]):
					return False
				else: 
					chave=roteiro[i]
					aeroporto=voos[chave]
			break
	return True
