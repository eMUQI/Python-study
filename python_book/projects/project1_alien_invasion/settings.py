class Settings():
    '''A class to store all the settings for the application'''

    def __init__(self):
        '''Initialize the game settings'''
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)  # 230,230,230 38,167,255

        # Ship settings
        self.life_limit = 3

        # bullet settings
        self.bullet_width = 3  # 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 8

        # alien settings
        self.fleet_drop_speed = 8  # 8

        # speed
        self.speed_up_scale = 1.2
        # score
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # initialize settings
        self.alien_speed_factor = 0.2
        self.bullet_speed_factor = 0.9
        self.ship_speed_factor = 0.6
        # fleet_direction of 1 represents right;-1 represents left
        self.fleet_direction = 1
        # score
        self.alien_points = 5

    def increase_speed(self):
        ''' increase alines's speed and score each alien '''
        self.alien_speed_factor *= self.speed_up_scale
        self.bullet_speed_factor *= self.speed_up_scale
        self.ship_speed_factor *= self.speed_up_scale
        # print("self.alien_speed_factor "+str(self.alien_speed_factor))

        self.alien_points = int(self.score_scale*self.alien_points)
