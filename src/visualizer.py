import pygame
import sys
import random

# config
SCREEN_SIZE = 100
SCALE = 5
FPS = 1

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

while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    for x, num in enumerate(arr):
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

pygame.quit()
sys.exit()