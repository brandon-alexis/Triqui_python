import pygame
from os.path import join

class Cell:
    def __init__(self, x, y, w, h):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect() 
        self.rect.topleft = (x, y)
        self.color = pygame.Color(255, 0, 0)
        self.shape = None
        self.font = pygame.font.Font(join("assets", "fonts", "Doto.ttf"), 100)
    
    def draw(self, container):
       pygame.draw.rect(container, self.color, self.rect) 
       
       if self.shape != None:
            text = self.font.render(self.shape, True, pygame.Color(255, 255, 255))  
            container.blit(text, (self.rect.centerx - text.get_width() // 2, self.rect.centery - text.get_height() // 2))
    
    def click(self, shape):
        if self.shape == None:
            self.shape = shape
            self.color = pygame.Color(0, 255, 0)
            
    def hover(self):
        if self.shape == None:
            self.color = pygame.Color(0, 0, 255)
    
    def not_hover(self):
        if self.shape == None:
            self.color = pygame.Color(255, 0, 0)