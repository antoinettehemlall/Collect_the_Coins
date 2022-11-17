import pygame

class Car:

    def __init__(self, cc_game):
        self.screen = cc_game.screen
        self.screen_rect = cc_game.screen.get_rect()

        self.image = pygame.image.load('images/Car-2-icon.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        self.screen.blit(self.image, self.rect)