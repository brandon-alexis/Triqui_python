import pygame
from cell import Cell
from settings import *

class Board:
    def __init__(self, x, y, size):
        self.surface = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
        self.rect = self.surface.get_rect() 
        self.rect.center = (x, y)
        self.color = BOARD_COLOR_BACKGROUND
        self.board = []
        self.size = size
        self.cell_size = (self.rect.width - (self.size - 1) * CELL_MARGIN) / self.size
        self.turn = CELL_SHAPE_X
        self.is_full = True
        self.winner = None
        self.setup()
    
    def setup(self):
        self.board = [[Cell(
            ((self.cell_size + CELL_MARGIN) * x) + self.rect.x, 
            ((self.cell_size + CELL_MARGIN) * y) + self.rect.y, 
            self.cell_size, 
            self.cell_size
        ) for x in range(self.size)] for y in range(self.size)]

    def draw(self, container):
        pygame.draw.rect(container, self.color, self.rect)
        
        for row in self.board:
            for cell in row:
               cell.draw(container) 
               
    def update(self):
        x, y = pygame.mouse.get_pos()        
        
        for row in self.board:
            for cell in row:
                if cell.rect.collidepoint(x, y):
                    cell.hover()
                else:
                    cell.not_hover()
            
    def change_turn(self):
        self.turn = CELL_SHAPE_O if self.turn == CELL_SHAPE_X else CELL_SHAPE_X
        print(self.turn)
        
    def check_winner(self, shape):
        for row in range(self.size):
            if self.board[row][0].shape == shape and self.board[row][1].shape == shape and self.board[row][2].shape == shape:
                self.winner = shape    
            
            for col in range(self.size):
                if self.board[0][col].shape == shape and self.board[1][col].shape == shape and self.board[2][col].shape == shape:
                    self.winner = shape
                    
                if self.board[0][0].shape == shape and self.board[1][1].shape == shape and self.board[2][2].shape == shape:
                    self.winner = shape
                
                if self.board[0][2].shape == shape and self.board[1][1].shape == shape and self.board[2][0].shape == shape:
                    self.winner = shape
                    
            is_full = True
            for row in range(self.size):
                for col in range(self.size):
                    if self.board[row][col].shape is None:  
                        is_full = False
                        break
                    
                    if not is_full:
                        break

            if is_full and self.winner is None:
                self.winner = "Empate" 
            
                    
    def is_board_complet(self):
        for row in self.board:
            for cell in row:
                if cell.shape != None:
                    return False
                
        return True
    
    def reset(self):
        self.turn = CELL_SHAPE_O if self.turn == CELL_SHAPE_O else CELL_SHAPE_X
        self.winner = None
        self.setup()

    def reset_all(self):
        self.turn = CELL_SHAPE_X
        self.winner = None
        self.setup()
                
                
                
                

                
                