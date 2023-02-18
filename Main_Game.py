import pygame
from Game_Logic import Tetris
from Render import *

class MyGame():
    def __init__(self, difficulty):

        pygame.init()

        self.gameSize = (400, 500)
        self.screen = pygame.display.set_mode(self.gameSize)

        pygame.display.set_caption("Tetris")

        self.difficulty = difficulty
        self.exitGame = False
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.game = Tetris(20, 12, self.difficulty)
        self.counter = 0

        self.pressing_down = False

    def start(self):
        while not self.exitGame:
            self.play()

        pygame.quit()

    def play(self):
        if self.game.figure is None:
            self.game.newFigure()
        self.counter += 1

        if self.counter > 100000:
            self.counter = 0

        if self.counter % (self.fps // self.game.level // 2) == 0 or self.pressing_down:
            if self.game.state == "start":
                self.game.go_down()

        self.keyPress()

        renderGame(self.game, self.screen)
        
        self.clock.tick(self.fps)



    def keyPress(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exitGame = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.game.rotate()
                if event.key == pygame.K_DOWN:
                    self.pressing_down = True
                if event.key == pygame.K_LEFT:
                    self.game.go_side(-1)
                if event.key == pygame.K_RIGHT:
                    self.game.go_side(1)
                if event.key == pygame.K_SPACE:
                    self.game.go_space()
                if event.key == pygame.K_ESCAPE:
                    #if game is paused
                        
                    #unpause game
                    self.game.__init__(20, 12, self.difficulty)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.pressing_down = False
