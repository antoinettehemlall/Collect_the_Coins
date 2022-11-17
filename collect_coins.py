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

        self.bg_color = (230, 230, 230)

        self.car = Car(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.car.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    cc = CollectCoins()
    cc.run_game()

