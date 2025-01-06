# game1.py
import pygame
from os.path import join

from player import Player
from config import *
from text_display import DisplayText


class MainGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Screen dimensions and setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("game")

        # Create a player instance
        self.player = Player()

        # Create a text instance
        self.text_display = DisplayText(self.screen)

        # Clock for controlling the frame rate
        self.clock = pygame.time.Clock()

        # Game loop control flag
        self.running = True

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

    def draw(self):
        # Clear screen
        self.screen.fill("cadetblue1")

        # Draw the player
        self.player.draw(self.screen)

        # Display text
        self.text_display.display_text("text", (SCREEN_WIDTH / 2, 100))

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
