import pygame
import sys
import random
import algorithms

# config
SCREEN_SIZE = 50
SCALE = 10
FPS = 60

# init 
pygame.init()
pygame.display.set_caption("sorting visualization")
screen = pygame.display.set_mode((SCREEN_SIZE * SCALE, SCREEN_SIZE * SCALE))
clock = pygame.time.Clock()

running = True

def generate_array(size):
    arr = list(range(1, size + 1))

    for i in range(size - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]

    return arr

arr = generate_array(SCREEN_SIZE)
sort = algorithms.bubble_sort(arr)

while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    try:
        screen.fill((0,0,0))
        
        for x, num in enumerate(next(sort)):
            pygame.draw.rect(
                screen, (255,255,255), (
                    x * SCALE, 
                    SCREEN_SIZE * SCALE - num * SCALE, 
                    SCALE, 
                    num * SCALE
                    )
            )

        pygame.display.flip()
        clock.tick(FPS)
        
    except StopIteration: # a funcao nao tem mais nenhum yield para retornar
        pygame.time.wait(5000)
        pygame.quit()
        sys.exit()