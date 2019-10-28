# Universidade Federal de Campina Grande - UFCG
# Programação 1 - 2019.2
# Guilherme Aureliano

def merge_invertido(l1, l2):
    array = []
    for e in l1:
        array.append(e)
    for e in l2:
        array.append(e)
        
    def sort(array):
        sort_half(array, 0, len(array) - 1)
        
    def sort_half(array, start, end):
        if start >= end:
            return
        
        middle = (start + end) // 2
        sort_half(array, start, middle)
        sort_half(array, middle + 1, end)
        
        merge(array, start, end)
        
    def merge(array, start, end):
        array[start: end + 1] = sorted(array[start: end + 1])
        
    sort(array)
    array_invertido = []
    for i in range(len(array) -1, -1, -1):
        array_invertido.append(array[i])
    return array_invertido

