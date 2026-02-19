'''
cada altoritmo vai retornar apenas os indices que devem ser trocados no array

por padrao, cade yield deve ser: "yield (<indices>,) <evento>"
    indices = um set com os indices que foram afetados 
    evento = uma string com a operacao/evento: "swap" | "shift" | "compare" | "pivot" | "ordered"
'''

def bubble_sort(arr):
    arr = arr.copy() # criamos uma copia so para o algoritmo usar
    size = len(arr)

    for i in range(size): # precisamos percorrer todo o array
        swapped = False

        for j in range(size-i-1): # para nao gerar indexError
            if arr[j] > arr[j+1]: # se o numero da frente eh menor, troca com o atual
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                yield (j, j+1), "swap"

        if not swapped: # se nao houveram trocas, esta ordenado
            break


def insertion_sort(arr):
    arr = arr.copy() # criamos uma copia so para o algoritmo

    for i in range(1,len(arr)): # comecamos no 1 pois assumimos que 0 esta ordenado
        current = arr[i] # guardamos o valor do item que esta em i
        j = i - 1 # uma casa antes
        
        while current < arr[j] and j >= 0: # quebra se acharmos um numero menor que o atual
            arr[j+1] = arr[j] # movemos o numero que comparamos uma casa para frente
            yield (j+1, j), "shift"
            j-=1 # vamos diminuindo ate achar um numero menor, ou chegarmos em -1
            
        arr[j+1] = current # coloamos o atual na frente de onde achamos um numero menor que ele


def selection_sort(arr):
    arr = arr.copy()
    size = len(arr)
    
    for i in range(size - 1): # vamos percorrer ate o penultimo, o ultimo fica ordenado
        pivot = i # assumimos que o menor elemento eh o i
        
        for j in range(i + 1, size): # vamos percorrer de i + 1 ate o fim
            yield (j, pivot), "compare"
            if arr[j] < arr[pivot]: # se o valor de j for menor, temos um novo menor
                pivot = j
                
        if i != pivot: # verifica se o menor ja esta no lugar certo, ou seja, i
            arr[i], arr[pivot] = arr[pivot], arr[i] # realizamos a troca
            yield (i, pivot), "swap"


def quick_sort(arr):
    arr = arr.copy()
    
    def partition(arr, start, end):
        pivot = arr[end] # ultimo elemento como pivo
        i = start - 1 # temos que comecar sempre 1 atras
        yield (end,), "pivot"
        
        for j in range(start, end):
            yield (j, end), "compare"
            if arr[j] < pivot: # trocamos caso seja menor
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                yield (i, j), "swap"
                
        # precisamos colocar o pivo na sua pos correta, que eh 1 na frente do i
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        yield (i + 1, end), "swap"
        
        return i + 1 # retornamos a pos do pivo
            
    def sort(arr, start, end):
        if start < end: # se for igual é False, ou seja, tem 1 elemento apenas
            pivot_index = yield from partition(arr, start, end) 
            
            yield from sort(arr, start, pivot_index - 1) # esquerda (menores)
            yield from sort(arr, pivot_index + 1, end) # direita (maiores)
            
    yield from sort(arr, 0, len(arr)-1) 
    # aqui, o 'yield from' retorna os yields que serao gerados em partition()
    # ele serve para repassar os yields para quem chamou a funcao
