import pygame
from cell import Cell

class Board:
    def __init__(self, x, y, w, h, size):
        self.surface = pygame.Surface((w, h))
        self.rect = self.surface.get_rect() 
        self.rect.center = (x, y)
        self.color = pygame.Color(255, 255, 255)
        self.board = []
        self.size = size
        self.cell_size = self.rect.width / self.size
        self.turn = "X"
        self.winner = None
        self.setup()
    
    def setup(self):
        self.board = [[Cell((self.cell_size * x) + self.rect.x, (self.cell_size * y) + self.rect.y, self.cell_size, self.cell_size) for x in range(self.size)] for y in range(self.size)]

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
        self.turn = "O" if self.turn == "X" else "X"
        
    def check_winner(self, shape):
        for row in range(self.size):
            # Check rows
            if self.board[row][0].shape == shape and self.board[row][1].shape == shape and self.board[row][2].shape == shape:
                self.winner = shape    
            
            for col in range(self.size):
                # Check rows
                if self.board[0][col].shape == shape and self.board[1][col].shape == shape and self.board[2][col].shape == shape:
                    self.winner = shape
                    
                # Check diagonal 1
                if self.board[0][0].shape == shape and self.board[1][1].shape == shape and self.board[2][2].shape == shape:
                    self.winner = shape
                
                # Check diagonal 2
                if self.board[0][2].shape == shape and self.board[1][1].shape == shape and self.board[2][0].shape == shape:
                    self.winner = shape
            
                    
    def is_board_complet(self):
        for row in self.board:
            for cell in row:
                if cell.shape != None:
                    return False
                
        return True
    
    def reset(self):
        self.turn = "O" if self.turn == "O" else "X"
        print(self.turn)
        self.winner = None
        self.board = [[Cell((self.cell_size * x) + self.rect.x, (self.cell_size * y) + self.rect.y, self.cell_size, self.cell_size) for x in range(self.size)] for y in range(self.size)]

                
                
                
                

                
                