import pygame, sys, algorithms
from render import Render
from state import Array
        
# config
SIZE = 128
SCALE = 4
FPS = 60
STEP = 1/200

# init 
pygame.init()
pygame.display.set_caption("sorting visualization")
screen = pygame.display.set_mode((SIZE * SCALE, SIZE * SCALE))
clock = pygame.time.Clock()

# geramos nosso array e embaralhamos ele
array = Array(SIZE)
array.shuffle()

# geramos o render e desenhamos o array todo
render = Render(screen, SCALE, SIZE)
render.draw_full(array.values)

# sort vai armazenar nossa funcao geradora
sort = algorithms.selection_sort(array.values)

timer = 0
running = True

while running:   
    dt = clock.tick(FPS) / 1000.0
    timer += dt
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    while timer >= STEP:
        try:
            position, operation = next(sort) # indices e a operacao que foi realizada
            
            array.operate(position, operation)
            render.update_bars(array.values, position, operation) # atualiza apenas as barras afetadas
            
            pygame.display.flip()
            
        except StopIteration: # a funcao nao tem mais nenhum yield para retornar
            running = False
        
        timer -= STEP
        
pygame.quit()
sys.exit()