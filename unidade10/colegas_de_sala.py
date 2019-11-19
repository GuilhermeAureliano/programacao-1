# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def colegas_de_sala(salasprofs, nome):
    referencia = 0
    for k, v in salasprofs.items():
        if nome == k:
            referencia = v
    lista = []
    for k, v in salasprofs.items():
        if v == referencia and k != nome:
            lista += [k]
    return lista
