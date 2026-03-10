import pygame
from render import BASE_COLORS
from state import VisualizerState

class UIRender:
    def __init__(self, screen: pygame.Surface, stats_rect: pygame.Rect, controls_rect: pygame.Rect):
        self.screen = screen
        self.stats_rect = stats_rect
        self.controls_rect = controls_rect
        self.font = pygame.font.SysFont("consolas", 14)

    def __draw_text(self, text: str, x: int, y: int):
        surface = self.font.render(text, True, (255,255,255))
        self.screen.blit(surface, (x, y))

    def draw_stats(self, state: VisualizerState, array: list[int]):
        pygame.draw.rect(self.screen, BASE_COLORS['background'], self.stats_rect)

        padding = 15
        y = self.stats_rect.y + 15

        self.__draw_text(f"{state.name}", self.stats_rect.width - 75 - padding, y)

        self.__draw_text(f"Accesses: {str(array.accesses)}", self.stats_rect.x + padding, y)

        self.__draw_text(f"Comparisons: {str(array.comparisons)}", self.stats_rect.x + 145, y)

        self.__draw_text(f"Swaps: {str(array.swaps)}", self.stats_rect.x + 300, y)

    def __draw_selector(self, rect: pygame.Rect, text: str, left_symbol: str, right_symbol: str):
        center_y = rect.centery

        left_surf = self.font.render(left_symbol, True, (200,200,200))
        right_surf = self.font.render(right_symbol, True, (200,200,200))
        text_surf = self.font.render(text, True, (255,255,255))

        padding = 20

        left_rect = left_surf.get_rect()
        right_rect = right_surf.get_rect()
        text_rect = text_surf.get_rect()

        left_rect.center = (rect.x + padding, center_y)
        right_rect.center = (rect.right - padding, center_y)
        text_rect.center = rect.center

        self.screen.blit(left_surf, left_rect)
        self.screen.blit(right_surf, right_rect)
        self.screen.blit(text_surf, text_rect)
        
    def draw_controls(self, size: int, algorithm_name: str, speed: int):
        pygame.draw.rect(self.screen, BASE_COLORS['background'], self.controls_rect)

        third_width = self.controls_rect.width // 3

        left_rect = pygame.Rect(
            self.controls_rect.x,
            self.controls_rect.y,
            third_width,
            self.controls_rect.height
        )

        center_rect = pygame.Rect(
            self.controls_rect.x + third_width,
            self.controls_rect.y,
            third_width,
            self.controls_rect.height
        )

        right_rect = pygame.Rect(
            self.controls_rect.x + third_width * 2,
            self.controls_rect.y,
            third_width,
            self.controls_rect.height
        )

        self.__draw_selector(left_rect, str(size), "↑", "↓")

        self.__draw_selector(center_rect, algorithm_name, "←", "→")

        self.__draw_selector(right_rect, f"{speed} op/s", "-", "+")
        