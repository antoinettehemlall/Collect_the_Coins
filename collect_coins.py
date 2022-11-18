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
            self.car.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = True
        if event.key == pygame.K_LEFT:
            self.car.moving_left = True
        if event.key == pygame.K_UP:
            self.car.moving_up = True
        if event.key == pygame.K_DOWN:
            self.car.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.car.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.car.moving_left = False
        if event.key == pygame.K_UP:
            self.car.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.car.moving_down = False

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.car.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    cc = CollectCoins()
    cc.run_game()

