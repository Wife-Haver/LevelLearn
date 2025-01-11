
import pygame
from os.path import dirname,join
from config import *
import random
from text_display import DisplayText






class Zone(pygame.Rect):
    def __init__(self, color, x_pos, y_pos, width, height):
        super().__init__()
        self.color = color
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height



    def draw(self,surf):
        pygame.draw.rect(surf,self.color,        #rectangle surface and color
                   (self.x,self.y,          #rectangle x and y position
                         self.width,self.height))#rectangle width and height


class Game_logic:

    def __init__(self):
        self.stem_list = ["Engineering", "Chemistry", "Physics", "Sciences", "Calculus"]
        self.abm_list = ["Marketing", "Finance", "Economics", "Business", "Accountancy"]
        self.ict_list = ["Programming", "Cybersecurity", "Software", "App Development", "Coding"]
        self.humss_list = ["Social Science", "Psychology", "Society", "Philosophy", "Literature"]

        self.points = 0

    def present_word(self):
        global chosen_word
        global chosen_list
        all_lists = [self.stem_list, self.abm_list, self.ict_list, self.humss_list]
        chosen_list = random.choice(all_lists)
        chosen_word = random.choice(chosen_list)
        print("WORD:" + chosen_word)

    def get_word(self):
        return chosen_word

    def get_strand(self):
        return chosen_list

    def get_points(self):
        return self.points



    def check_answer(self,current_zone):
        word = self.get_word()
        list = self.get_strand()
        strand = ""



        if word in self.stem_list:
            strand = "stem"
        elif word in self.abm_list:
            strand = "abm"
        elif word in self.ict_list:
            strand = "ict"
        elif word in self.humss_list:
            strand = "humss"
        else:
            strand = "None"

        if current_zone == strand:
            print("CORRECT")
            self.points += 1
        else:
            print("WRONG")












