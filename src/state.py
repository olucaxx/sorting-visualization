import random

class Array:
    def __init__(self, size):
        self.values = list(range(1, size + 1))

    def swap(self, i, j):
        '''
        troca dois elementos de posicao
        '''
        self.values[i], self.values[j] = self.values[j], self.values[i]
        
    def shuffle(self):
        '''
        gera uma permutacao aleatoria, garante que todos os elementos tentem trocar de lugar
        '''
        for i in range(len(self.values) - 1, 0, -1): 
            self.swap(i, random.randint(0, i))
            
            