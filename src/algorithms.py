'''
cada altoritmo vai retornar apenas os indices que devem ser trocados no array
'''

def bubble_sort(arr):
    arr = arr.copy() # criamos uma copia so para o algoritmo usar
    size = len(arr)

    for i in range(size): # precisamos percorrer todo o array
        swapped = False

        for j in range(size-i-1): # para nao gerar indexError
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                yield j, j+1 # retorna apenas os indices que trocaram

        if not swapped: # se nao houveram trocas, esta ordenado
            break
