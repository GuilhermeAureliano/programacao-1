# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def flip(l,i,j):
  while i <= j:
    l[i],l[j] = l[j],l[i]
    i += 1
    j -= 1 
