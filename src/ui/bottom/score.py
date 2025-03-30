import pygame
from ui.text import Text
from settings import *

class Score:
    def __init__(self, x, y, w, h, color, score, title):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect()
        self.rect.center = (x ,y)
        self.color = color
        self.score = score
        self.ui_text = Text(self.rect.centerx - 40, y, FONT_NAME_ROBOTO, title, 15, TEXT_WHITE)
        self.ui_score = Text(self.ui_text.x + self.ui_text.surface.get_width() + FONT_MARGIN, y, FONT_NAME_DOTO, str(self.score), 20, TEXT_WHITE)
        
        
    def draw(self, container: pygame.Surface):
        pygame.draw.rect(container, self.color, self.rect)
    
        self.ui_text.draw(container)
        self.ui_score.draw(container)
    
    def update(self, new_score): 
        self.score = str(new_score)
        self.ui_score.update(self.score)
        