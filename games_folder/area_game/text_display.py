import pygame


class DisplayText:
   def __init__(self,screen,font_size):
      self.font = pygame.font.Font(None,font_size)
      self.screen = screen



   def display_text(self,text,pos,color):
      self.text = text
      self.pos = pos
      self.color = color
      self.text_surf = self.font.render(self.text, True,self.color   )
      self.text_rect = self.text_surf.get_rect()
      self.text_rect.center = self.pos
      self.screen.blit(self.text_surf, self.text_rect)

