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
            self.draw_bar(x, v, (255,255,255))

    def draw_bar(self, x, value, color):
        '''
        desenha apenas uma barra branca na tela
        '''
        pygame.draw.rect(
            self.screen,
            color,
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

    def update_bars(self, arr, pos, op):
        '''
        encapsula a atualizacao de barras, apagar + desenhar
        '''
        if op == "swap" or op == "shift":
            for x in pos:
                self.clear_bar(x)
                self.draw_bar(x, arr[x], (255,255,255))
        
