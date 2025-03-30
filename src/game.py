import pygame, sys
from board import Board
from ui.top.shapes_box import ShapesBox
from ui.top.turn_box import TurnBox
from ui.top.reset_button import ResetButton
from ui.bottom.score import Score
from ui.top.winner_title import WinnerTitle
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
        self.turn_box = TurnBox(self.WINDOW_WIDTH / 2, WINDOW_MARGIN * 2, 100, 50, BACKGROUND_BLACK, self.board.turn)
        self.reset_button = ResetButton(self.WINDOW_WIDTH - WINDOW_MARGIN, WINDOW_MARGIN, 50, 50)
        self.score_x = Score(WINDOW_MARGIN * 3, self.WINDOW_HEIGHT - 50, 100, 50, SCORE_COLOR_BACKGROUND_X, self.board.score_x, "Gano X")
        self.score_o = Score(self.WINDOW_WIDTH - 50 - WINDOW_MARGIN, self.score_x.rect.centery, 100, 50, SCORE_COLOR_BACKGROUND_O, self.board.score_o, "Gano O")
        self.score_tie = Score(self.WINDOW_WIDTH / 2, self.score_x.rect.centery, 100, 50, SCORE_COLOR_BACKGROUND_TIE, self.board.score_tie, "Empate")
        self.winner_title = WinnerTitle(self.WINDOW_WIDTH, 100, (0, 0, 0), "") 
        
    def setup(self):
        pygame.display.set_caption(WINDOW_TITLE) 
        
    def update(self):
        self.board.update()
        self.turn_box.update(self.board.turn)
        self.score_x.update(self.board.score_x)
        self.score_o.update(self.board.score_o)
        self.score_tie.update(self.board.score_tie)
    
    def draw(self):
        self.board.draw(self.window) 
        self.shapes_box.draw(self.window)
        self.turn_box.draw(self.window)
        self.reset_button.draw(self.window)
        self.score_x.draw(self.window)
        self.score_o.draw(self.window)
        self.score_tie.draw(self.window)
        self.winner_title.draw(self.window)


    
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
                                        
                    self.board.incrementScoreX() if self.board.winner == CELL_SHAPE_X else None
                    self.board.incrementScoreO() if self.board.winner == CELL_SHAPE_O else None
                    
                    self.winner_title.update(f"{self.board.winner} Gano!", SCORE_COLOR_BACKGROUND_X if self.board.winner == CELL_SHAPE_X else SCORE_COLOR_BACKGROUND_O)
                else:
                    print(self.board.winner)
                    self.board.incrementScoreTie()
                    
                    self.winner_title.update("Empate", SCORE_COLOR_BACKGROUND_TIE)
                    
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
                    
                                
                        