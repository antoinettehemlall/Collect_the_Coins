import pygame

class Coin:

    def __init__(self, cc_game):
        """Set starting position"""
        self.screen = cc_game.screen
        self.settings = cc_game.settings
        self.screen_rect = cc_game.screen.get_rect()

        self.image = pygame.image.load('images/coin.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)