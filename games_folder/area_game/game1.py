# game1.py
import pygame
from os.path import join, dirname

from player import Player
from config import *
from text_display import DisplayText
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

        # Game logic
        self.game_logic = Game_logic()

        self.stem_image = pygame.image.load("stem.png")
        self.abm_image = pygame.image.load("abm.png")
        self.ict_image = pygame.image.load("ict.png")
        self.humss_image = pygame.image.load("humss.png")

        # Creating zones
        self.stem_area = self.stem_image.get_rect()
        self.stem_area.topleft = (150, 100)

        self.abm_area = self.abm_image.get_rect()
        self.abm_area.topleft = (425, 100)

        self.ict_zone = self.ict_image.get_rect()
        self.ict_zone.topleft = (150, 375)

        self.humss_zone = self.humss_image.get_rect()
        self.humss_zone.topleft = (425, 375)
        self.text_display = DisplayText(self.screen, 48)

        # Points/score text
        self.score_label = DisplayText(self.screen, 36)

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        # Define the timer event
        self.TIMER_EVENT = pygame.USEREVENT + 1
        self.TIMER_INTERVAL = 5000  # 5 seconds
        pygame.time.set_timer(self.TIMER_EVENT, self.TIMER_INTERVAL)

        # Time remaining
        self.start_time = pygame.time.get_ticks()
        self.time_left = self.TIMER_INTERVAL // 1000  # Initial time in seconds

        # Game loop control flag
        self.running = True
        self.current_zone = ""

        # Score tracking
        self.previous_score = 0
        self.score = 0

        # "+1" text fade settings
        self.plus_one_opacity = 0
        self.plus_one_duration = 1000  # Fade duration in milliseconds
        self.plus_one_start_time = None

        # Initial run
        self.game_logic.present_word()
        global rand_word
        rand_word = self.game_logic.get_word()

    def get_current_zone(self):
        return self.current_zone

    def get_score(self) -> int:
        return self.score

    def handle_events(self):
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == self.TIMER_EVENT:
                # Reset timer and call game logic
                self.start_time = pygame.time.get_ticks()
                self.game_logic.check_answer(self.current_zone)
                self.game_logic.present_word()

    def update(self):
        # Get pressed keys
        keys = pygame.key.get_pressed()

        # Move the player
        self.player.move(keys)

        # Determine the current zone
        if self.stem_area.contains(self.player.frect):
            self.current_zone = "stem"
        elif self.abm_area.contains(self.player.frect):
            self.current_zone = "abm"
        elif self.ict_zone.contains(self.player.frect):
            self.current_zone = "ict"
        elif self.humss_zone.contains(self.player.frect):
            self.current_zone = "humss"
        else:
            self.current_zone = "None"

        # Check and update score
        self.score = self.game_logic.get_points()
        if self.score > self.previous_score:
            self.plus_one_start_time = pygame.time.get_ticks()
            self.plus_one_opacity = 255  # Fully visible at first
            self.previous_score = self.score

        # Handle "+1" fade-out effect
        if self.plus_one_start_time is not None:
            elapsed = pygame.time.get_ticks() - self.plus_one_start_time
            if elapsed < self.plus_one_duration:
                # Gradually decrease opacity
                self.plus_one_opacity = max(0, 255 - int((elapsed / self.plus_one_duration) * 255))
            else:
                self.plus_one_opacity = 0
                self.plus_one_start_time = None  # Stop displaying "+1"

        # Update the timer display
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        self.time_left = max(0, (self.TIMER_INTERVAL - elapsed_time) // 1000)

    def draw(self):
        # Clear screen
        self.screen.fill("cadetblue1")

        # Draw zones
        self.screen.blit(self.stem_image, self.stem_area)
        self.screen.blit(self.abm_image, self.abm_area)
        self.screen.blit(self.ict_image, self.ict_zone)
        self.screen.blit(self.humss_image, self.humss_zone)

        # Draw the player
        self.player.draw(self.screen)

        # Display word
        self.text_display.display_text(self.game_logic.get_word(), (SCREEN_WIDTH / 2, 50), "black")

        # Display points text
        self.score_label.display_text("Score:" + str(self.score), (60, 50), "black")

        # Render and display the timer
        font = pygame.font.Font(None, 36)
        timer_text = font.render(f"Time Left: {self.time_left}s", True, "red")
        self.screen.blit(timer_text, (SCREEN_WIDTH - 200, 40))

        # Display "+1" text with fading effect
        if self.plus_one_opacity > 0:
            plus_one_font = pygame.font.Font(None, 48)
            plus_one_surface = plus_one_font.render("+1", True, (0, 255, 0))
            plus_one_surface.set_alpha(self.plus_one_opacity)  # Set transparency
            self.screen.blit(plus_one_surface, (90,50))

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
