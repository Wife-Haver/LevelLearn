# game1.py

import pygame
from os.path import join, dirname

from player import Player
from config import *
from text_display import DisplayText
import areas
from areas import Game_logic




class MainGame:


    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions and setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("game")



        # Create a player instance
        self.player = Player()

        #game lcoic
        self.game_logic = Game_logic()


        self.stem_image = pygame.image.load(join(dirname(__file__),"game_assets/areas/stem.png"))
        self.abm_image = pygame.image.load(join(dirname(__file__),"game_assets/areas/abm.png"))
        self.ict_image = pygame.image.load(join(dirname(__file__),"game_assets/areas/ict.png"))
        self.humss_image = pygame.image.load(join(dirname(__file__),"game_assets/areas/humss.png"))

        #creating zones
        self.stem_area = self.stem_image.get_frect()
        self.stem_area.topleft=(150,100)

        self.abm_area = self.abm_image.get_frect()
        self.abm_area.topleft = (425,100)

        self.ict_zone = self.ict_image.get_frect()
        self.ict_zone.topleft = (150,375)

        self.humss_zone = self.humss_image.get_frect()
        self.humss_zone.topleft = (425,375)
        self.text_display = DisplayText(self.screen,48)

        #points/score text
        self.score_label = DisplayText(self.screen,36)


        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        #variable for timer
        self.start_time = pygame.time.get_ticks()
        self.last_present_time = None  # Track the last time `areas.present_word()` was run
        self.present_word_delay = 10000  # Delay in milliseconds (10 seconds)

        # Game loop control flag
        self.running = True
        self.current_zone = ""

        current_time = pygame.time.get_ticks()
        self.last_present_time = current_time

        #initital run
        self.game_logic.present_word()
        global rand_word
        rand_word = self.game_logic.get_word()
        #print(rand_word)

    def get_current_zone(self):
        return self.current_zone

    def get_score(self) -> int:
        return self.score


    def handle_events(self):
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        # Get pressed keys
        keys = pygame.key.get_pressed()

        # Move the player
        self.player.move(keys)

        if self.stem_area.contains(self.player.frect):
            self.current_zone = "stem"
        elif self.abm_area.contains(self.player.frect):
            self.current_zone = "abm"
        elif self.ict_zone.contains(self.player.frect):
            self.current_zone = "ict"
        elif self.humss_zone.contains(self.player.frect):
            self.current_zone = "humss"
        else:
            self.current_zone="None"

        # score
        self.score = self.game_logic.get_points()


        # for choosing new word/checking answer
        current_time = pygame.time.get_ticks()
        if self.last_present_time is not None and current_time - self.last_present_time >= self.present_word_delay:
            self.game_logic.check_answer(self.current_zone)
            self.game_logic.present_word()
            rand_word = self.game_logic.get_word()
            #print(rand_word)

            self.last_present_time = current_time



        #timer for remaining time

        timer_duration = 10000
        elapsed_time = pygame.time.get_ticks() - self.start_time
        self.time_left = max(0, (timer_duration - elapsed_time) // 1000)
        font = pygame.font.Font(None, 36)
        self.timer_text = font.render(f"Time Left: {self.time_left}s", True, "red")

        if self.time_left == 0:
            self.start_time = current_time

    def draw(self):
        # Clear screen
        self.screen.fill("cadetblue1")

        #drawing zones
        self.screen.blit(self.stem_image,self.stem_area)
        self.screen.blit(self.abm_image,self.abm_area)
        self.screen.blit(self.ict_image,self.ict_zone)
        self.screen.blit(self.humss_image,self.humss_zone)

        # Draw the player
        self.player.draw(self.screen)

        # Display word
        self.text_display.display_text(self.game_logic.get_word(), (SCREEN_WIDTH / 2, 50),"black")

        #timer
        self.screen.blit(self.timer_text, (SCREEN_WIDTH-160, 40))

        #points text
        self.score_label.display_text("Score:" + str(self.score),(60,50),"black")

        # Update the display
        pygame.display.flip()

    def run(self):
        # Game loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)  # Cap the frame rate


        # Quit Pygame when the game loop ends
        pygame.quit()


if __name__ == "__main__":
    game = MainGame()
    game.run()
