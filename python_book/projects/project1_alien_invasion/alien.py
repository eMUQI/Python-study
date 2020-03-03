import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        ''' create an alien with ship'''
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and get its rect
        self.image = pygame.image.load('images/ufo-space-ship-alien.bmp')
        self.rect = self.image.get_rect()

        # start eac new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's excat position
        self.x = float(self.rect.x)

        # store the alien's gap
        self.aliens_gap = self.rect.width/2
        self.alien_border_gap = self.rect.width/2

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        ''' return true if alien is at the edge of screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True

    def update(self):
        ''' move the alien '''
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
