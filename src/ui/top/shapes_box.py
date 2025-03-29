from ui.text import Text
from settings import *

class ShapesBox:
    def __init__(self, x, y):
        self.ui_text_x = Text(x, y, FONT_NAME_DOTO, CELL_SHAPE_X, 50, BACKGROUND_SECONDARY)
        self.ui_text_o = Text(x + self.ui_text_x.surface.get_width() + FONT_MARGIN, y, FONT_NAME_DOTO, CELL_SHAPE_O, 50, BACKGROUND_TERCIARY)
    
    def draw(self, container: pygame.Surface):
        self.ui_text_x.draw(container)
        self.ui_text_o.draw(container)