import pygame
import sys
from pygame.sprite import Sprite
from random import randint

class Star:
    """Manage star pic."""

    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Alien_Invation")
        # Load pic
        # self.image1 = pygame.image.load('pic//star.jpg')

        # Star settings
        self.star_width = 3
        self.star_height = 3
        self.bullet_color = (255,255,255)

        # Background settings
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (60,60,60)

    def _update_screen(self):
        """Update image on the screen, and flip to new screen."""
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.screen.fill(self.bg_color)
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()

if __name__ == "__main__":
    ai = Star()
    ai.run()

