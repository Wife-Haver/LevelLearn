
import pygame
from os.path import join,dirname


from config import *



class Player:
    def __init__(self):
        self.image = pygame.image.load(join(dirname(__file__),"game_assets/players_sprites/down/1.png"))
        self.image = pygame.transform.scale(self.image, (48, 68))
        self.speed = PLAYER_SPEED
        self.frect = self.image.get_frect()
        self.frect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    def draw(self, screen):
        screen.blit(self.image,self.frect)


    def move(self, keys):
        dx, dy = 0, 0#represents horizontal and vertical movement

        #Handle input/update dx and dy
        if keys[pygame.K_UP] and self.frect.top > 0:
            dy = -1
        if keys[pygame.K_DOWN] and self.frect.bottom < SCREEN_HEIGHT:
            dy = 1
        if keys[pygame.K_LEFT] and self.frect.left > 0:
            dx = -1
        if keys[pygame.K_RIGHT] and self.frect.right < SCREEN_WIDTH:
            dx = 1

        # Normalize vector if moving diagonally
        if dx != 0 and dy != 0:
            magnitude = (dx ** 2 + dy ** 2) ** 0.5
            dx /= magnitude
            dy /= magnitude

        # Update position with consistent speed
        self.frect.x += int(dx * self.speed)
        self.frect.y += int(dy * self.speed)


