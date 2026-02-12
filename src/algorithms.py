'''
cada altoritmo vai retornar o estado do array a cada mudanca, iteracao ou comparacao
'''

def bubble_sort(arr):
    size = len(arr)

    for i in range(size): # precisamos percorrer todo o array
        swapped = False
        
        yield arr

        for j in range(size-i-1): # para nao gerar indexError
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                yield arr

        if not swapped: # se nao houveram trocas, esta ordenado
            yield arr
            break
