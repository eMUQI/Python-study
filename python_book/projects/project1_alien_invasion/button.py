import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        ''' initialize button '''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #  set button's dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (117, 218, 173)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build button's rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # button msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        ''' Draw the button and massage '''
        # Draw the button
        self.screen.fill(self.button_color, self.rect)
        # Draw the massage image
        self.screen.blit(self.msg_image, self.msg_image_rect)
