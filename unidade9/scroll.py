# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def scroll(m):
	for i in range(len(m) - 1):
		m[i], m[i + 1] = m[i + 1], m[i]
	for i in range(len(m)):
		for j in range(len(m[0])):
			if i == len(m) - 1:
				m[i][j] *= 0
	return m
  
m = [[1,2,3],
     [4,5,6],
     [7,8,9],
     [10, 11, 12]]
assert scroll(m) == [[4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12],
                    [0, 0, 0]]
