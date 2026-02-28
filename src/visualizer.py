# bibliotecas python
import pygame, sys
from enum import Enum
from collections import deque

# imports do projeto
import algorithms as algorithms_module
from render import AlgorithmRender
from state import SortingArray

MIN_SIZE, MIN_SCALE, MAX_SIZE, MAX_SCALE = 16, 32, 512, 1

class VisualizerState(Enum):
    IDLE = 1 # vai representar um estado parado
    RUNNING = 2 # vai representar um estado de ordenacao, permitindo pausas, etc
    RENDERING = 3 # vai representar um estado de renderizacao, que nao permite pausas, etc
    PAUSED = 4 # vai permitir diferenciar de quando o algoritmo foi pausado ou finalizado

class Visualizer():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("sorting visualization")
        self.screen = pygame.display.set_mode((MAX_SCALE * MAX_SIZE, MAX_SCALE * MAX_SIZE)) 
        self.clock = pygame.time.Clock()
        self.window_loop = True 
        
        self.size = MIN_SIZE * 4
        self.scale = MIN_SCALE / 4
        
        self.speed = self.size
        self.change_step()
        self.last_step = 0
        
        self.algorithms = deque([
            ("bubble", algorithms_module.bubble_sort),
            ("selection", algorithms_module.selection_sort),
            ("insertion", algorithms_module.insertion_sort),
            ("quick", algorithms_module.quick_sort),
        ])
        
        self.current_algorithm = self.algorithms[0]
        self.algorithm_name = self.current_algorithm[0]
        
        self.reset_array()
        self.render.fill_background()
        
    def change_algorithm(self, direction):
        if self.state != VisualizerState.IDLE:
            return
    
        if direction in (-1, 1):
            self.algorithms.rotate(direction)
            self.current_algorithm = self.algorithms[0]
            print(self.current_algorithm[0])
        
    def render_array(self):
        self.runner = algorithms_module.render_array(self.array)
        
        self.timer = 0 
        self.last_step = self.step
        self.step = 1 / (self.size * 3) 
           
        self.state = VisualizerState.RENDERING
    
    def shuffle_array(self):
        if self.state in (VisualizerState.RENDERING, VisualizerState.RUNNING):
            return
        
        self.array.clear_stats()
        self.runner = algorithms_module.shuffle(self.array)
        
        self.timer = 0 
        self.last_step = self.step
        self.step = 1 / (self.size * 2)
        
        self.state = VisualizerState.RENDERING
    
    def reset_array(self):
        self.array = SortingArray(self.size)
        self.render = AlgorithmRender(self.screen, self.scale, self.size)
        
        self.render_array()
        
    def run_algorithm(self):
        if self.state == VisualizerState.RENDERING:
            return
        
        if self.state == VisualizerState.RUNNING:
            self.state = VisualizerState.PAUSED
            return
        
        if self.state == VisualizerState.IDLE:
            self.runner = self.current_algorithm[1](self.array)
            self.algorithm_name = self.current_algorithm[0]
            self.array.clear_stats()
        
        self.timer = 0 
        self.state = VisualizerState.RUNNING 
        
    def increase_size(self):
        if self.state in (VisualizerState.RENDERING, VisualizerState.RUNNING):
            return
        
        if self.size < MAX_SIZE: 
            self.size = int(self.size * 2)
            self.scale = int(self.scale / 2)  
            self.reset_array()
        
    def decrease_size(self):
        if self.state in (VisualizerState.RENDERING, VisualizerState.RUNNING):
            return
        
        if self.size > MIN_SIZE: 
            self.size = int(self.size / 2)
            self.scale = int(self.scale * 2)
            self.reset_array()

    def change_step(self):
        print(self.speed)
        self.step = 1 / self.speed

    def increase_speed(self):
        self.speed *= 2
        self.change_step()

    def decrease_speed(self):
        if self.speed > 1:
            self.speed = int(self.speed / 2)
            self.change_step()

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
                        self.shuffle_array()
                        
                    if event.key == pygame.K_KP_ENTER:
                        self.run_algorithm()
                        
                    if event.key == pygame.K_UP:
                        self.increase_size()
                                            
                    if event.key == pygame.K_DOWN:
                        self.decrease_size()
                        
                    if event.key == pygame.K_LEFT:
                        self.change_algorithm(-1)
                            
                    if event.key == pygame.K_RIGHT:
                        self.change_algorithm(1)
                        
                    if event.key == pygame.K_KP_PLUS:
                        self.increase_speed()
                        
                    if event.key == pygame.K_KP_MINUS:
                        self.decrease_speed()
                        
            if self.state != VisualizerState.IDLE and self.state != VisualizerState.PAUSED:
                while self.timer >= self.step:
                    try:
                        position, event = next(self.runner) # retorn os indices e o evento que ele(s) se refere(m)
                        self.render.update_bars(self.array.values, position, event)
                                    
                    except StopIteration: # a funcao nao tem mais nenhum yield para retornar
                        self.state = VisualizerState.IDLE
                    
                    self.timer -= self.step

                if self.state == VisualizerState.IDLE:
                    self.render.update_bars(self.array.values, [], None) # apenas para limpeza
                    
                    if self.last_step > 0: # caso tenhamos armazendo um step temporario, ex. renderizacao
                        self.step = self.last_step
                        self.last_step = 0

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = Visualizer()
    visualizer.run()