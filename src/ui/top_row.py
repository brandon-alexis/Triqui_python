import pygame
from ui.text import Text
from ui.turn_box import TurnBox
from settings import *

class TopRow:
    def __init__(self, x, y, w, h, turn):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)
        self.turn = turn
        self.color = BACKGROUND_PRIMARY
        self.ui_text_x = Text(x, self.rect.centery, FONT_NAME_DOTO, CELL_SHAPE_X, 50, BACKGROUND_SECONDARY)
        self.ui_text_o = Text(x + self.ui_text_x.surface.get_width() + FONT_MARGIN, self.rect.centery, FONT_NAME_DOTO, CELL_SHAPE_O, 50, BACKGROUND_TERCIARY)
        self.ui_turn_box = TurnBox(self.rect.centerx, self.rect.centery, 80, 50, BACKGROUND_BLACK, self.turn)
    
    def draw(self, container: pygame.Surface):
        pygame.draw.rect(container, self.color, self.rect)
        self.ui_text_x.draw(container)
        self.ui_text_o.draw(container)
        self.ui_turn_box.draw(container)
        
        
    def update_turn(self, turn):
        self.ui_turn_box.set_turn(turn)
        
    
        