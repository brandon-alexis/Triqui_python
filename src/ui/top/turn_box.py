import pygame
from ui.text import Text
from settings import *

class TurnBox:
    def __init__(self, x, y, w, h, color, turn):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect()
        self.rect.center = (x, y)
        self.color = color
        self.turn = turn
        self.ui_text = Text(self.rect.left + FONT_MARGIN, y, FONT_NAME_ROBOTO, "Turn", 20, TEXT_WHITE)
        self.ui_turn = Text(self.rect.left + self.ui_text.surface.get_width() + FONT_MARGIN * 1.5, y, FONT_NAME_ROBOTO, self.turn, 20, TEXT_WHITE)
        
    def draw(self, container: pygame.Surface):
        pygame.draw.rect(container, self.color, self.rect)
    
        self.ui_text.draw(container)
        self.ui_turn.draw(container)
        
    def update(self, turn): 
        self.turn = turn 
        self.ui_turn.update(self.turn)
        
        
        
        
        