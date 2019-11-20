# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

medidas = {'km':1000, 'hm':100, 'dam':10, 'm':1,
           'dm':0.1,'cm':0.01, 'mm':0.001}
while True:
    x = input().split()
    soma = (int(x[0]) * medidas[x[1]]) + (int(x[2]) * medidas[x[3]])
    if soma == 0: break
    print('{:.2f} m'.format(soma))
