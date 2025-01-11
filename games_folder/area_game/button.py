import pygame

class Button:
    def __init__(self, x, y, width, height, text='', text_color="black",
                 bg_color=(0, 0, 255), hover_color=(0, 0, 200), border_radius=5):
        """
        Initializes the button.

        :param x: X-coordinate of the button's top-left corner.
        :param y: Y-coordinate of the button's top-left corner.
        :param width: Width of the button.
        :param height: Height of the button.
        :param text: Text displayed on the button.
        :param text_color: Color of the text (RGB tuple).
        :param bg_color: Background color of the button (RGB tuple).
        :param hover_color: Background color when the button is hovered (RGB tuple).
        :param border_radius: Radius for rounded corners.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_size = 40
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.border_radius = border_radius

        self.font = pygame.font.Font(None, self.font_size)  # Use default font

    def draw(self, screen):
        """
        Draws the button on the screen.

        :param screen: Pygame screen surface.
        """
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        color = self.hover_color if is_hovered else self.bg_color

        # Draw button background
        pygame.draw.rect(screen, color, self.rect, border_radius=self.border_radius)

        # Render text
        if self.text:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        """
        Checks if the button is clicked.

        :param event: Pygame event object.
        :return: True if the button is clicked, False otherwise.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
