import pygame

class Car:

    def __init__(self, cc_game):
        """Set starting position"""
        self.screen = cc_game.screen
        self.settings = cc_game.settings
        self.screen_rect = cc_game.screen.get_rect()

        self.image = pygame.image.load('images/Car-2-icon.png')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the car's position based on movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.car_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.car_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.car_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.car_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)