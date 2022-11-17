import sys

import pygame

from settings import Settings
from car import Car

class CollectCoins:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Collect the Coins!")

        self.car = Car(self)

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()



    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.car.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    cc = CollectCoins()
    cc.run_game()

