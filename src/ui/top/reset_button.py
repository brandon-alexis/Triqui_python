import pygame
from settings import *

class ResetButton:
    def __init__(self, x, y, w, h):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect() 
        self.rect.topright = (x, y)
        self.color = BUTTON_COLOR_BACKGROUND 
        self.font = BUTTON_FONT
        self.text_color = BUTTON_COLOR_TEXT
        self.text = "R"
        self.sound_click = RESET_SOUND
        self.sound_hover = CELL_SOUND_HOVER
        self.sound_played = False
    
    def draw(self, container: pygame.Surface):
       pygame.draw.rect(container, self.color, self.rect) 
       
       text = self.font.render(self.text, True, self.text_color)  
       container.blit(text, (self.rect.centerx - text.get_width() // 2, self.rect.centery - text.get_height() // 2))
    
    def click(self):
        self.sound_click.play()
        return True
    
            
    def hover(self):
        self.color = BUTTON_COLOR_BACKGROUND_HOVER
        self.text_color = BUTTON_COLOR_TEXT_HOVER
        
        if not self.sound_played:
            self.sound_hover.play()
            self.sound_played = True
    
    def not_hover(self):
        self.color = BUTTON_COLOR_BACKGROUND
        self.text_color = BUTTON_COLOR_TEXT
        
        self.sound_played = False
