class GameStats():
    ''' trace statistics for alien_invasion'''

    def __init__(self, ai_settings):
        ''' initialize statistics '''
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        ''' initialize statistics '''
        self.life = self.ai_settings.life_limit
