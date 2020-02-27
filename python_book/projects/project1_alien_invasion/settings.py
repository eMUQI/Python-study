class Settings():
    '''A class to store all the settings for the application'''

    def __init__(self):
        '''Initialize the game settings'''
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230) #230,230,230 38,167,255
        
        # Ship settings
        self.ship_speed_factor = 0.5
        self.life_limit = 3

        # bullet settings
        self.bullet_speed_factor = 0.7
        self.bullet_width = 800 #3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 5

        # alien settings
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 60
        # fleet_direction of 1 represents right;-1 represents left
        self.fleet_direction = -1


