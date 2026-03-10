import pygame

BASE_COLORS = {
    'background': (15,15,15), # quase preto, cinza bem escuro
    'start': (80,100,110), # ciano sei la
    'end': (255,255,255), # brancao
    'ordered': (80,255,120), # verde bonito
}

EVENT_COLORS = {    
    'swap': (255,0,0), # vermelho
    'compare': (255,255,0), # amarelo
    'pivot': (120,0,255), # roxo
}

class AlgorithmRender:
    def __init__(self, screen: pygame.Surface, rect: pygame.Rect, scale: int, height: int):
        self.screen = screen
        self.rect = rect
        self.scale = scale 
        self.height = height 
        
        self.last_changes = set() 
        
    def __default_color(self, value: int):
        t = (value-1)/(self.height-1)

        start = BASE_COLORS['start']
        end = BASE_COLORS['end']

        r = int(start[0] + (end[0]-start[0])*t)
        g = int(start[1] + (end[1]-start[1])*t)
        b = int(start[2] + (end[2]-start[2])*t)

        return (r,g,b)
    
    def __clear_bar(self, x: int):
        '''
        apaga uma barra da tela (pinta a coluna inteira de preto)
        '''
        pygame.draw.rect(
            self.screen,
            BASE_COLORS['background'],
            (
                self.rect.x + x * self.scale,
                self.rect.y,
                self.scale,
                self.rect.height
            )
        )

    def __draw_bar(self, x: int, value: int, color: set[int, int, int]):
        '''
        desenha apenas uma barra branca na tela
        '''
        bar_height = value * self.scale
        
        pygame.draw.rect(
            self.screen,
            color,
            (
                self.rect.x + x * self.scale,
                self.rect.y + self.rect.height - bar_height,
                self.scale,
                bar_height
            )
        )
        
    def __redraw_bar(self, x: int, value: int, color: set[int, int, int]):
        '''
        encapsula a atualizacao de barras: apagar + desenhar
        '''
        self.__clear_bar(x)
        self.__draw_bar(x, value, color)
        
    def draw_full(self, arr: list[int]):
        '''
        desenha todo o array inicial
        '''
        self.fill_background()
        for x, v in enumerate(arr):
            self.__draw_bar(x, v, self.__default_color(v))

    def update_bars(self, arr: list[int], positions: set[int], event: str):
        '''
        logica para desenhar as operacoes realizadas no array
        '''
        for x in self.last_changes:
            self.__redraw_bar(x, arr[x], self.__default_color(arr[x]))
            
        self.last_changes.clear()
        
        if event == "draw":
            i = positions[0]
            self.__redraw_bar(i, arr[i], self.__default_color(arr[i]))
        
        if event in EVENT_COLORS:
            for ev in positions:
                self.__redraw_bar(ev, arr[ev], EVENT_COLORS[event])
                self.last_changes.add(ev)
        