
class AlgorithmRunner:
    def __init__(self, generator):
        self.generator = generator
        self.finished = False
        
    def step(self):
        if self.finished: # finalizou, nao tem oq retornar
            return None
        try:
            return next(self.generator) # retorn os indices e o evento que ele(s) se refere(m)      
                          
        except StopIteration: # a funcao nao tem mais nenhum yield para retornar
            self.finished = True
            return None
