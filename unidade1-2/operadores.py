# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Operadores

a = int(input())
b = int(input())

adicao = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a/b
resto = a % b
expo = a ** b

print('===== Operadores =====')

print('A =',a)
print('B =',b)

print('Adição =',adicao)
print('Subtração =',subtracao)
print('Multiplicação =',multiplicacao)
print('Divisão =','%.0f' % divisao)
print('Resto =',resto)
print('Exponenciação =',expo)
print('Negação de A =',-a)

# a função bool retorna valores True ou False
igual = bool(a == b)
diferente = bool(a !=b)
maiorA = bool(a>b)
maiorB = bool(b > a)
menor = bool(a <= b)

print('A é igual a B?',igual)
print('A é diferente de B?',diferente)
print('A é maior que B?',maiorA)
print('B é maior que A?',maiorB)
print('A é menor ou igual a B?',menor)


