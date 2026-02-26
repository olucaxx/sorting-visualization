import random
from state import SortingArray

'''
cada altoritmo vai retornar apenas os indices que devem ser trocados no nosso renderizador

dentro dos algoritmos ele devera alterar as informacoes de acesso, comparacao e troca do obj SortingArray

por padrao, cade yield deve ser: "yield (<indices>,) <evento>"  
    indices = um set com os indices que foram afetados 
    evento = uma string com a operacao/evento: "swap" | "compare" | "pivot" | "draw"
'''

def render_array(array: SortingArray):
    for i in range(array.size):
        yield (i,), "draw"
        
def shuffle(array: SortingArray):
    for i in range(array.size - 1, 0, -1):
        j = random.randint(0, i)
        array.swap(i, j)
        yield (i, j), "swap"

def bubble_sort(array: SortingArray):
    for i in range(array.size): # precisamos percorrer todo o array
        swapped = False

        for j in range(array.size - i - 1): # para nao gerar indexError
            if array.compare(array.get(j) > array.get(j+1)): # se o numero da frente eh menor, troca com o atual
                array.swap(j, j+1)
                swapped = True
                yield (j, j+1), "swap"

        if not swapped: # se nao houveram trocas, esta ordenado
            break


def insertion_sort(array: SortingArray):
    for i in range(1, array.size): # comecamos no 1 pois assumimos que 0 esta ordenado
        current = array.get(i) # guardamos o valor do item que esta em i
        j = i - 1 # uma casa antes
        
        while j >= 0: # limite 
            j_value = array.get(j) # separamos do and para conseguir contabilizar apenas 1 acesso
            comparison = array.compare(current < j_value) # nao vamos renderizar a comparacao, fica melhor assim
            
            if not comparison: # quebra se acharmos um numero menor que o atual
                break
            
            array.set(j+1, array.get(j)) # movemos o numero que comparamos uma casa para frente
            yield (j+1, j), "swap"
            j-=1 # vamos diminuindo ate achar um numero menor, ou chegarmos em -1
            
        array.set(j+1, current) # coloamos o atual na frente de onde achamos um numero menor que ele


def selection_sort(array: SortingArray):
    for i in range(array.size - 1): # vamos percorrer ate o penultimo, o ultimo fica ordenado
        pivot = i # assumimos que o menor elemento eh o i
        
        for j in range(i + 1, array.size): # vamos percorrer de i + 1 ate o fim
            comparison = array.compare(array.get(j) < array.get(pivot) )
            yield (j, pivot), "compare"
            if comparison: # se o valor de j for menor, temos um novo menor
                pivot = j
                
        if i != pivot: # verifica se o menor ja esta no lugar certo, ou seja, i
            array.swap(i, pivot) # realizamos a troca
            yield (i, pivot), "swap"


def quick_sort(array: SortingArray):
    def partition(array, start, end):
        pivot = array.get(end) # ultimo elemento como pivo
        yield (end,), "pivot"
        i = start - 1 # temos que comecar sempre 1 atras
        
        for j in range(start, end):
            comparison = array.compare(array.get(j) < pivot)
            yield (j, end), "compare"
            if comparison: # trocamos caso seja menor
                i += 1
                array.swap(i, j)
                yield (i, j), "swap"
                
        # precisamos colocar o pivo na sua pos correta, que eh 1 na frente do i
        array.swap(i + 1, end)
        yield (i + 1, end), "swap"
        
        return i + 1 # retornamos a pos do pivo
            
    def sort(array, start, end):
        if start < end: # se for igual é False, ou seja, tem 1 elemento apenas
            pivot_index = yield from partition(array, start, end) 
            
            yield from sort(array, start, pivot_index - 1) # esquerda (menores)
            yield from sort(array, pivot_index + 1, end) # direita (maiores)
            
    yield from sort(array, 0, len(array.values)-1) 
    # aqui, o 'yield from' retorna os yields que serao gerados em partition()
    # ele serve para repassar os yields para quem chamou a funcao
