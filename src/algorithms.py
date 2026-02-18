'''
cada altoritmo vai retornar apenas os indices que devem ser trocados no array

por padrao, cade yield deve retornar:
    um set com os indices que foram afetados 
    uma string com a operacao: "swap" | "shift" | "compare"
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
