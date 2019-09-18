# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

um = int(input())
dois = int(input())
tres = int(input())

soma = um + dois + tres

if soma % 3 == 0 and soma % 5 !=0 :
    print('plif')

elif soma % 5 == 0 and soma % 3 != 0:
    print('plof')

elif soma % 3 == 0 and soma % 5 == 0:
    print('plifplof')

else:
    print(soma)
