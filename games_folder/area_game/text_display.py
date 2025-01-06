import pygame
import time
import random
from os.path import join,dirname

from config import *


class DisplayText:
   def __init__(self,screen):
      self.font = pygame.font.Font(None,48)
      self.screen = screen


   def display_text(self,text,pos):
      self.text = text
      self.pos = pos
      self.text_surf = self.font.render(self.text, True, "black")
      self.text_rect = self.text_surf.get_rect()
      self.text_rect.center = self.pos
      self.screen.blit(self.text_surf, self.text_rect)

