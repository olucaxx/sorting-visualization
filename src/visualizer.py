import pygame, sys, algorithms
from render import Render
from state import Array
from runner import AlgorithmRunner
        
# start config
size = 128 
scale = 4
step = 1/100

# init 
pygame.init()
pygame.display.set_caption("sorting visualization")
screen = pygame.display.set_mode((size * scale, size * scale)) # 512x512
clock = pygame.time.Clock()

# geramos nossas instancias iniciais
array = Array(size)
render = Render(screen, scale, size)
runner = AlgorithmRunner(algorithms.render_array(array.values))
rendering = True

timer = 0
running = True
rendering = False

temp_step = 0

while running:   
    dt = clock.tick(60) / 1000.0
    timer += dt
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    runner = AlgorithmRunner(algorithms.shuffle(array.values))
                    temp_step = step
                    step = 1 / (size * 2)
                    timer = 0
                    rendering = True
                    
                if event.key == pygame.K_KP_ENTER:
                    runner = AlgorithmRunner(algorithms.quick_sort(array.values))
                    timer = 0
                    
                if event.key == pygame.K_UP:
                    if size < 512: # o scale fica menor que 1 a partir disso
                        size = int(size * 2)
                        scale = int(scale / 2)  
                        array = Array(size)
                        render = Render(screen, scale, size)
                        runner = AlgorithmRunner(algorithms.render_array(array.values))
                        timer = 0
                        temp_step = step
                        step = 1 / (size * 3)
                        rendering = True
                                        
                if event.key == pygame.K_DOWN:
                    if size > 16: # minimo bom, menor que isso fica irrelevante'
                        size = int(size / 2)
                        scale = int(scale * 2)
                        array = Array(size)
                        render = Render(screen, scale, size)
                        runner = AlgorithmRunner(algorithms.render_array(array.values))
                        timer = 0
                        temp_step = step
                        step = 1 / (size * 3)
                        rendering = True
    
    while timer >= step and not runner.finished:
        result = runner.step()
        
        if result is not None:
            position, event = result
            
            array.operate(position, event)
            render.update_bars(array.values, position, event) # atualiza apenas as barras afetadas
            
        timer -= step

    if runner.finished: 
        render.update_bars(array.values, [], None) # vamos limpar o ultimo evento
        
        if rendering:
            rendering = False
            step = temp_step
        
    pygame.display.flip()

pygame.quit()
sys.exit()