class Settings():
    '''A class to store all the settings for the application'''

    def __init__(self):
        '''Initialize the game settings'''
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230) #230,230,230 38,167,255
        self.ship_speed_factor = 0.5

        # bullet settings
        self.bullet_speed_factor = 0.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5
