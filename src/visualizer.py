# bibliotecas python
import pygame, sys
from enum import Enum

# imports do projeto
import algorithms
from render import AlgorithmRender
from state import Array
from runner import AlgorithmRunner

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
        self.state = VisualizerState.IDLE
        
        # inicializacao de controladores
        self.array = Array(self.size)
        self.render = AlgorithmRender(self.screen, self.scale, self.size)
        self.runner = AlgorithmRunner(algorithms.render_array(self.array.values))
        
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
                        self.runner = AlgorithmRunner(algorithms.shuffle(self.array.values))
                        self.temp_step = self.step
                        self.step = 1 / (self.size * 2)
                        self.timer = 0
                        self.state = VisualizerState.RUNNING
                        
                    if event.key == pygame.K_KP_ENTER:
                        self.runner = AlgorithmRunner(algorithms.quick_sort(self.array.values))
                        self.timer = 0
                        
                    if event.key == pygame.K_UP:
                        if self.size < 512: # o scale fica menor que 1 a partir disso
                            self.size = int(self.size * 2)
                            self.scale = int(self.scale / 2)  
                            self.array = Array(self.size)
                            self.render = AlgorithmRender(self.screen, self.scale, self.size)
                            self.runner = AlgorithmRunner(algorithms.render_array(self.array.values))
                            self.timer = 0
                            self.temp_step = self.step
                            self.step = 1 / (self.size * 3)
                            self.state = VisualizerState.RUNNING
                                            
                    if event.key == pygame.K_DOWN:
                        if self.size > 16: # minimo bom, menor que isso fica irrelevante'
                            self.size = int(self.size / 2)
                            self.scale = int(self.scale * 2)
                            self.array = Array(self.size)
                            self.render = AlgorithmRender(self.screen, self.scale, self.size)
                            self.runner = AlgorithmRunner(algorithms.render_array(self.array.values))
                            self.timer = 0
                            self.temp_step = self.step
                            self.step = 1 / (self.size * 3)
                            self.state = VisualizerState.RUNNING

            while self.timer >= self.step and not self.runner.finished:
                result = self.runner.step()

                if result is not None:
                    position, event = result

                    self.array.operate(position, event)
                    self.render.update_bars(self.array.values, position, event)

                self.timer -= self.step

            if self.runner.finished:
                self.render.update_bars(self.array.values, [], None)
                self.state = VisualizerState.IDLE

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = Visualizer(16, 32, 512, 1)
    visualizer.run()