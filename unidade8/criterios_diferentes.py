# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def ordena(lista1,lista2):
  new = []
  i = 0
  j = len(lista2) - 1
  while True:
    if i == len(lista1) or j == -1:
      break
    
    if lista1[i] > lista2[j]:
      new.append(lista2[j])
      j -= 1
    else:
      new.append(lista1[i])
      i += 1

  if i != len(lista1):
    for e in range(i, len(lista1)):
      new.append(lista1[e])
  else:
    for e in range(len(lista2) -1, -1, -1):
      new.append(lista2[e])

  return new 
