import pygame
from ui.text import Text
from settings import *

class WinnerTitle:
    def __init__(self, width, height, color, text):
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.title_text = Text(self.width / 2 - 74 * 2, self.height / 2, FONT_NAME_DOTO, self.text, 74, (255, 255, 255))
        self.visible = False
        self.time_visible = 0
        self.sound = WINNER_SOUND
        self.sound_played = False
        self.setup()
        
    def setup(self):
        self.sound.set_volume(0.8)

    def update(self, text, color, show_duration=1.5):
        self.text = text
        self.color = color
        self.title_text.update(self.text)
        self.title_text.color = (255, 255, 255)
        self.visible = True
        self.time_visible = pygame.time.get_ticks() + show_duration * 1000
        self.sound.play()

    def draw(self, container:pygame.Surface):
        if self.visible:
            pygame.draw.rect(container, self.color,self.rect) 
            self.title_text.draw(container)

            if pygame.time.get_ticks() >= self.time_visible:
                self.visible = False
