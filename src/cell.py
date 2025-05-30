import pygame
from settings import *

class Cell:
    def __init__(self, x, y, w, h):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect() 
        self.rect.topleft = (x, y)
        self.color = CELL_COLOR_BACKGROUND
        self.shape = None
        self.font = CELL_FONT
        self.sound = CELL_SOUND_HOVER
        self.sound_played = False
    
    def draw(self, container: pygame.Surface):
       pygame.draw.rect(container, self.color, self.rect) 
       
       if self.shape != None:
            text_color = None
            if self.shape == CELL_SHAPE_X:
                text_color = CELL_COLOR_TEXT_X
            else:
                text_color = CELL_COLOR_TEXT_O
                
            text = self.font.render(self.shape, True, text_color)  
            container.blit(text, (self.rect.centerx - text.get_width() // 2, self.rect.centery - text.get_height() // 2))
    
    def click(self, shape):
        if self.shape == None:
            self.shape = shape
            self.color = CELL_COLOR_ACTIVE
            return True
        
        return False
    
            
    def hover(self):
        if self.shape == None:
            self.color = CELL_COLOR_BACKGROUND_HOVER
            
            if not self.sound_played:
                self.sound.play()
                self.sound_played = True

    
    def not_hover(self):
        if self.shape == None:
            self.color = CELL_COLOR_BACKGROUND
            
            self.sound_played = False