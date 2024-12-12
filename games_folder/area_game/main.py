import pygame
import sys
from config import *
from debug import debug
from player import *
class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()


        self.player = Player(100,200,50,'red')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #input
            keys = pygame.key.get_pressed()
            self.player.move(keys)


            #drawing
            self.screen.fill('cadetblue1')
            self.player.draw(self.screen)





            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()