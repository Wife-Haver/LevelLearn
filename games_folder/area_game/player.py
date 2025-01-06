
import pygame
from os import walk
from os import path
from os.path import join,dirname

from PIL.ImageOps import scale
from pygame.examples.cursors import image

from config import *



class Player:
    def __init__(self):
        self.image =None
        self.load_images()
        self.state,self.frame_index = 'down',0
        self.color = "red"
        self.speed = PLAYER_SPEED
        #self.frect = self.image.get_frect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2))



    def load_images(self):
        self.frames ={"left":[],"right":[],"up":[],"down":[]}

        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join(dirname(__file__), 'game_assets\\players_sprites',state)):
                if file_names:
                    for file_name in sorted(file_names,key=lambda name:int(name.split('.')[0 ])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)


    def animate(self,dt):
        #get state

        #animate
        self.frame_index += 5*dt
        self.image  = self.frames[self.state][int(self.frame_index)%len(self.frames[self.state])]

    def draw(self, screen):
        pass

        #screen.blit(self.image,(100,100))



    def move(self, keys):
        dx, dy = 0, 0#represents horizontal and vertical movement

        # Handle input/update dx and dy
        # if keys[pygame.K_UP] and self.frect.top > 0:
        #     dy = -1
        # if keys[pygame.K_DOWN] and self.frect.bottom < SCREEN_HEIGHT:
        #     dy = 1
        # if keys[pygame.K_LEFT] and self.frect.left > 0:
        #     dx = -1
        # if keys[pygame.K_RIGHT] and self.frect.right < SCREEN_WIDTH:
        #     dx = 1

        # Normalize vector if moving diagonally
        if dx != 0 and dy != 0:
            magnitude = (dx ** 2 + dy ** 2) ** 0.5
            dx /= magnitude
            dy /= magnitude

        # Update position with consistent speed
        # self.frect.x += int(dx * self.speed)
        # self.frect.y += int(dy * self.speed)