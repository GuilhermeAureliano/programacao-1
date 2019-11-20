# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def num_creditos(bd_ufcg, matricula):
    soma = 0
    for chave, valor in bd_ufcg.items():
        for k, v in valor.items():
            if matricula in v:
                soma += k[1]
