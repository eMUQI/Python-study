import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        '''Initialize the ship and set its starting position'''
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/planes/plane9.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        # Store a decimal value for the ship's center
        self.centerx = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Update the ship's position based on the movement flah'''
        # update the ship's center value,not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor

        # update rect object from self.centerx
        self.rect.centerx = self.centerx

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # self.center = self.screen_rect.centerx
        # self.rect.centerx = self.screen_rect.centerx
        # can't use self.rect.centerx because it will be replace by self.center when update()
        self.centerx = self.screen_rect.centerx
        # print(self.rect.centerx,self.screen_rect.centerx,self.centerx,self.rect.center)
