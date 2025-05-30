import pygame
from os.path import join

# Configuraciones del juego
pygame.init()

# Configuracion de colores del juego
BACKGROUND_PRIMARY = "#222222"
BACKGROUND_SECONDARY = "#1abc9c"
BACKGROUND_TERCIARY = "#f1c40f"
BACKGROUND_WHITE = "#ffffff"
BACKGROUND_BLACK = "#2c3e50"
TEXT_PRIMARY = "#34495e"
TEXT_SECONDARY = "#1abc9c"
TEXT_TERCIARY = "#f1c40f"
TEXT_WHITE = "#ffffff"

# Configuraciones de fuentes del juego
FONT_NAME_DOTO = "Doto"
FONT_NAME_ROBOTO = "Roboto"
FONT_PATH_DOTO = join("assets", "fonts", "Doto.ttf")
FONT_PATH_ROBOTO = join("assets", "fonts", "Roboto.ttf")
FONT_MARGIN = 10

# Configuraciones de sonidos
SOUND_PATH_HOVER = join("assets", "sounds", "hover_cell_sound.mp3")
SOUND_PATH_VICTORY = join("assets", "sounds", "victory.ogg")
SOUND_PATH_RESET = join("assets", "sounds", "reset.wav")
SOUND_VOLUME = 1

# Configuraciones de botones del juego
BUTTON_COLOR_BACKGROUND = BACKGROUND_WHITE
BUTTON_COLOR_BACKGROUND_HOVER = TEXT_PRIMARY
BUTTON_COLOR_TEXT = TEXT_PRIMARY
BUTTON_COLOR_TEXT_HOVER = BACKGROUND_WHITE
BUTTON_FONT_SIZE = 20
BUTTON_FONT = pygame.font.Font(FONT_PATH_DOTO, BUTTON_FONT_SIZE)

# Configuraciones de ventana del juego
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 570
WINDOW_TITLE = "Triqui"
WINDOW_MARGIN = 25
WINDOW_COLOR_BACKGROUND = BACKGROUND_PRIMARY
WINDOW_ICON_PATH = join("assets", "images", "favicon.ico")
WINDOW_ICON = pygame.image.load(WINDOW_ICON_PATH)
FPS = 60

# Configuraciones de tablero del juego
BOARD_WIDTH = 350
BOARD_HEIGHT = 350
BOARD_COLOR_BACKGROUND = BACKGROUND_PRIMARY

# Configuraciones de las celdas del juego
CELL_MARGIN = 5
CELL_SHAPE_X = "X"
CELL_SHAPE_O = "O"
CELL_FONT_SIZE = 100
CELL_FONT = pygame.font.Font(FONT_PATH_DOTO, CELL_FONT_SIZE)
CELL_COLOR_BACKGROUND = BACKGROUND_BLACK
CELL_COLOR_BACKGROUND_HOVER = TEXT_PRIMARY
CELL_COLOR_ACTIVE = TEXT_PRIMARY
CELL_COLOR_TEXT_X = TEXT_SECONDARY 
CELL_COLOR_TEXT_O = TEXT_TERCIARY
CELL_SOUND_HOVER = pygame.mixer.Sound(SOUND_PATH_HOVER)

# Configuraciones de caja de puntajes
SCORE_COLOR_BACKGROUND_X = BACKGROUND_SECONDARY
SCORE_COLOR_BACKGROUND_O = BACKGROUND_TERCIARY
SCORE_COLOR_BACKGROUND_TIE = BACKGROUND_BLACK
SCORE_COLOR_TEXT = TEXT_PRIMARY
SCORE_FONT_SIZE = 20

# Configuraciones de titulo del ganador
WINNER_SOUND = pygame.mixer.Sound(SOUND_PATH_VICTORY) 

# Configuraciones de boton de reinicio
RESET_SOUND = pygame.mixer.Sound(SOUND_PATH_RESET)







