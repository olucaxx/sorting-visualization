import pygame

class Render:
    def __init__(self, screen, scale, height):
        self.screen = screen 
        self.scale = scale 
        self.height = height 

    def draw_full(self, arr):
        '''
        desenha todo o array inicial
        '''
        self.screen.fill((0,0,0))
        for x, v in enumerate(arr):
            self.draw_bar(x, v)

    def draw_bar(self, x, value):
        '''
        desenha apenas uma barra branca na tela
        '''
        pygame.draw.rect(
            self.screen,
            (255,255,255),
            (
                x * self.scale,
                self.height * self.scale - value * self.scale,
                self.scale,
                value * self.scale
            )
        )

    def clear_bar(self, x):
        '''
        apaga uma barra da tela (pinta a coluna inteira de preto)
        '''
        pygame.draw.rect(
            self.screen,
            (0,0,0),
            (x*self.scale, 0, self.scale, self.height*self.scale)
        )

    def update_bars(self, arr, i, j):
        '''
        encapsula a atualizacao de barras, apagar + desenhar
        '''
        for idx in (i, j):
            self.clear_bar(idx)
            self.draw_bar(idx, arr[idx])
