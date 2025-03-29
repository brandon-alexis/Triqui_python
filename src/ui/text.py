import pygame
from settings import *

class Text:
    def __init__(self, x, y, font_name, text, size, color):
        self.x = x
        self.y = y
        self.font_name = font_name
        self.text = text
        self.size = size
        self.color = color
        self.font = None
        self.surface = None
        self.setup()
        
    def setup(self):
        if self.font == None:
            if self.font_name == FONT_NAME_DOTO:
                self.font = pygame.font.Font(FONT_PATH_DOTO, self.size)
            elif self.font_name == FONT_NAME_ROBOTO:
                self.font = pygame.font.Font(FONT_PATH_ROBOTO, self.size)

            if self.surface == None:    
                self.surface = self.font.render(self.text, True, self.color)
                
    def draw(self, container: pygame.Surface):
        container.blit(self.surface, (self.x, self.y - self.surface.get_height() / 2))
    
    def update(self, text):
        self.text = text
        self.surface = self.font.render(self.text, True, self.color)
        