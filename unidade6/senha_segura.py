# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def senha_segura(senha):
    if len(senha) >= 4:
        pares, impares = 0, 0
        for i in range(len(senha)):
            if i % 2 == 0 and int(senha[i]) % 2 != 0:
                impares += 1
            elif i % 2 != 0 and int(senha[i]) % 2 == 0:
                pares += 1
        if (pares + impares) == len(senha):
            msg = 'Senha segura'
        else:
            msg = 'Senha insegura'
    else:
        msg = 'Senha insegura'
    return msg
