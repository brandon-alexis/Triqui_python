import pygame, sys
from board import Board
from ui.top.shapes_box import ShapesBox
from ui.top.turn_box import TurnBox
from ui.top.reset_button import ResetButton
from settings import *

class Game:
    def __init__(self):
        pygame.init() 
        self.WINDOW_WIDTH = WINDOW_WIDTH 
        self.WINDOW_HEIGHT = WINDOW_HEIGHT 
        self.color = WINDOW_COLOR_BACKGROUND 
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT)) 
        self.running = True 
        self.clock = pygame.Clock() 
        self.fps = 60 
        self.dt = 0 
        self.setup()
        
        self.board = Board((self.WINDOW_WIDTH / 2), self.WINDOW_HEIGHT / 2, size=3)
        self.shapes_box = ShapesBox(WINDOW_MARGIN, WINDOW_MARGIN * 2)
        self.turn_box = TurnBox(self.WINDOW_WIDTH / 2, WINDOW_MARGIN * 2, 80, 50, BACKGROUND_BLACK, self.board.turn)
        self.reset_button = ResetButton(self.WINDOW_WIDTH - WINDOW_MARGIN, WINDOW_MARGIN, 50, 50)
        
    def setup(self):
        pygame.display.set_caption(WINDOW_TITLE) 
        
    def draw(self):
        self.board.update()
        self.turn_box.update(self.board.turn)
    
    def update(self):
        self.board.draw(self.window) 
        self.shapes_box.draw(self.window)
        self.turn_box.draw(self.window)
        self.reset_button.draw(self.window)
    
    def run(self):
        while self.running: 
            self.window.fill(self.color) 
            
            self.dt = self.clock.tick(self.fps) / 1000 
            
            self.check_events()  
            
            # Update
            self.update()
                        
            # Draw
            self.draw()

                        
            # Check winner
            self.board.check_winner(CELL_SHAPE_X) 
            self.board.check_winner(CELL_SHAPE_O) 
            
            if self.board.winner != None:
                if self.board.winner == CELL_SHAPE_X or self.board.winner == CELL_SHAPE_O: 
                    print(f"{self.board.winner} Gano!")
                else:
                    print(self.board.winner)
                    
                self.board.reset()
            
            pygame.display.flip()
    
    def stop(self):
        self.running = False
        sys.exit(0)
        
    def reset(self):
        self.board.reset() 
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()  # Detener el juego
                
            x, y = pygame.mouse.get_pos()
            
            if self.reset_button.rect.collidepoint(x, y):
                self.reset_button.hover()
            else:
                self.reset_button.not_hover()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
            
                for row in self.board.board:
                    for cell in row:
                        if cell.rect.collidepoint(x, y):
                            if cell.click(self.board.turn):
                                self.board.change_turn()  # Cambiar el turno
                                
                if self.reset_button.rect.collidepoint(x, y):
                    if self.reset_button.click():
                        self.board.reset_all()
                    
                                
                        