# bibliotecas python
import pygame, sys
from enum import Enum

# imports do projeto
import algorithms
from render import AlgorithmRender
from state import SortingArray

class VisualizerState(Enum):
    IDLE = 1
    RUNNING = 2
    PAUSED = 3

class Visualizer():
    def __init__(self, MIN_SIZE, MIN_SCALE, MAX_SIZE, MAX_SCALE):
        
        # setup inicial
        pygame.init()
        pygame.display.set_caption("sorting visualization")
        self.screen = pygame.display.set_mode((MAX_SCALE * MAX_SIZE, MAX_SCALE * MAX_SIZE)) 
        self.clock = pygame.time.Clock()
        
        self.size = 128
        self.scale = 4
        self.step = 1/100

        self.timer = 0
        self.window_loop = True
        self.temp_step = 0
        
        # inicializacao de controladores
        self.array = SortingArray(self.size)
        self.render = AlgorithmRender(self.screen, self.scale, self.size)
        self.runner = algorithms.render_array(self.array)
        self.state = VisualizerState.RUNNING 
        
        # necessario pois o nosso fundo nao eh preto e fica estranho se nao renderizar antes
        self.render.fill_background()
        
    def change_size(self):
        pass
    
    def change_algorithm(self):
        pass
    
    def change_speed(self):
        pass
        
    def run(self):
        while self.window_loop:
            dt = self.clock.tick(60) / 1000.0
            self.timer += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.window_loop = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.array.clear_stats()
                        self.runner = algorithms.shuffle(self.array)
                        self.temp_step = self.step
                        self.step = 1 / (self.size * 2)
                        self.timer = 0
                        self.state = VisualizerState.RUNNING
                        
                    if event.key == pygame.K_KP_ENTER:
                        self.array.clear_stats()
                        self.runner = algorithms.quick_sort(self.array)
                        self.timer = 0
                        self.state = VisualizerState.RUNNING
                        
                    if event.key == pygame.K_UP:
                        if self.size < 512: # o scale fica menor que 1 a partir disso
                            self.size = int(self.size * 2)
                            self.scale = int(self.scale / 2)  
                            self.array = SortingArray(self.size)
                            self.render = AlgorithmRender(self.screen, self.scale, self.size)
                            self.runner = algorithms.render_array(self.array)
                            self.timer = 0
                            self.temp_step = self.step
                            self.step = 1 / (self.size * 3)
                            self.state = VisualizerState.RUNNING
                                            
                    if event.key == pygame.K_DOWN:
                        if self.size > 16: # minimo bom, menor que isso fica irrelevante'
                            self.size = int(self.size / 2)
                            self.scale = int(self.scale * 2)
                            self.array = SortingArray(self.size)
                            self.render = AlgorithmRender(self.screen, self.scale, self.size)
                            self.runner = algorithms.render_array(self.array)
                            self.timer = 0
                            self.temp_step = self.step
                            self.step = 1 / (self.size * 3)
                            self.state = VisualizerState.RUNNING
                            
            if self.state == VisualizerState.RUNNING:
                while self.timer >= self.step:
                    try:
                        position, event = next(self.runner) # retorn os indices e o evento que ele(s) se refere(m)

                        self.render.update_bars(self.array.values, position, event)
                                    
                    except StopIteration: # a funcao nao tem mais nenhum yield para retornar
                        self.state = VisualizerState.IDLE
                    
                    self.timer -= self.step

                if self.state == VisualizerState.IDLE:
                    self.render.update_bars(self.array.values, [], None)

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = Visualizer(16, 32, 512, 1)
    visualizer.run()