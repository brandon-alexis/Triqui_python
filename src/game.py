import pygame, sys
from board import Board

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.WINDOW_WIDTH = width 
        self.WINDOW_HEIGHT = height 
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.running = True
        self.clock = pygame.Clock()
        self.fps = 60
        self.dt = 0
        self.setup()
        
        self.board = Board(self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2, self.WINDOW_WIDTH -  200, self.WINDOW_HEIGHT - 200, size=3)
        
    def setup(self):
        pygame.display.set_caption("Game")
    
    def run(self):
        while self.running:
            self.window.fill(pygame.Color(25, 25, 25)) 
            self.dt = self.clock.tick(self.fps) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()     
                if event.type == pygame.KEYDOWN:
                    print(pygame.key)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.menu_screen.run()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    
                    for row in self.board.board:
                        for cell in row:
                            if cell.rect.collidepoint(x, y):
                                cell.click(self.board.turn)   
                                self.board.change_turn()   
                                
            self.board.draw(self.window)
            self.board.update() 
            self.board.check_winner("X")
            self.board.check_winner("O")
            
            if self.board.winner != None:
                print(f"{self.board.winner} Win!")
                self.board.reset()
        
            
            pygame.display.flip() 
    
    def stop(self):
        self.running = False
        sys.exit(0)
        
    def reset(self):
        print("X")
        self.board.reset()