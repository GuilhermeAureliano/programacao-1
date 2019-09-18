# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
media = (nota1 + nota2 + nota3) / 3

presenca = int(input())
faltas  = (presenca * 100) / 30
porcentagem = 100 - faltas

if porcentagem < 75:
    print('reprovado por faltas')

elif media < 4:
    print('reprovado por nota')

elif media >= 7 and porcentagem >= 75:
    print('aprovado por media')

else:
    print('prova final')

