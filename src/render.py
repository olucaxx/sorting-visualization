import pygame

class Render:
    def __init__(self, screen, scale, height):
        self.screen = screen 
        self.scale = scale 
        self.height = height 
        
        self.last_changes = set() 

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
        
    def redraw_bar(self, x, value, color):
        '''
        encapsula a atualizacao de barras: apagar + desenhar
        '''
        self.clear_bar(x)
        self.draw_bar(x, value, color)

    def update_bars(self, arr, positions, operation):
        '''
        logica para desenhar as operacoes realizadas no array
        '''
        if self.last_changes:
            for x in self.last_changes:
                self.redraw_bar(x, arr[x], (255,255,255))
            
        self.last_changes.clear()
        
        if operation == "compare":
            for c in positions:
                self.redraw_bar(c, arr[c], (255,255,0))
                self.last_changes.add(c)
        
        if operation == "swap" or operation == "shift":
            for s in positions:
                self.redraw_bar(s, arr[s], (255,0,0))
                self.last_changes.add(s)
