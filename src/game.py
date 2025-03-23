import pygame, sys
from board import Board
from ui.top_row import TopRow
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
        self.top_row = TopRow(WINDOW_MARGIN, WINDOW_MARGIN, self.WINDOW_WIDTH - WINDOW_MARGIN * 2, 70, self.board.turn)
        
    def setup(self):
        pygame.display.set_caption(WINDOW_TITLE)
    
    def run(self):
        while self.running:
            self.window.fill(self.color) 
            self.dt = self.clock.tick(self.fps) / 1000
            
            self.check_events()  
                                
            self.board.draw(self.window)
            self.board.update() 
            self.board.check_winner(CELL_SHAPE_X)
            self.board.check_winner(CELL_SHAPE_O)
            self.top_row.draw(self.window)
           
            
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
                    self.stop()     
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    
                    for row in self.board.board:
                        for cell in row:
                            if cell.rect.collidepoint(x, y):
                                if cell.click(self.board.turn):
                                    self.board.change_turn() 
                                
                        