import sys

import pygame

from settings import Settings

class CollectCoins:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Collect the Coins!")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """Update images on the screen"""
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

if __name__ == '__main__':
    cc = CollectCoins()
    cc.run_game()

