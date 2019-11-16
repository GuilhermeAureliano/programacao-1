# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def meu_in(v, professor):
	for e in v:
		if e == professor: return True

def disciplinas(alocacao, professor):
	cont = 0
	cadeiras = []
	for k, v in alocacao.items():
		if meu_in(v, professor):
			for e in v:
				if e == professor:
					cont += k[1]
			cadeiras.append(k[0])
	return (cadeiras, cont)
