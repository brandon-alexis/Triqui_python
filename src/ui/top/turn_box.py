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
        self.ui_text = Text(self.rect.centerx - 40, y, FONT_NAME_ROBOTO, "Turno", 20, TEXT_WHITE)
        self.ui_turn = Text(self.ui_text.x + self.ui_text.surface.get_width() + FONT_MARGIN, y, FONT_NAME_DOTO, self.turn, 20, TEXT_WHITE)
        
    def draw(self, container: pygame.Surface):
        pygame.draw.rect(container, self.color, self.rect)
    
        self.ui_text.draw(container)
        self.ui_turn.draw(container)
        
    def update(self, new_turn): 
        self.turn = new_turn 
        self.ui_turn.update(self.turn)
        
        
        
        
        