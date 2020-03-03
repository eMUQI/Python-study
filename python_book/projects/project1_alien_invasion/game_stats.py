class GameStats():
    ''' trace statistics for alien_invasion'''

    def __init__(self, ai_settings):
        ''' initialize statistics '''
        self.high_score = 0
        self.ai_settings = ai_settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        ''' initialize statistics '''
        self.life = self.ai_settings.life_limit
        self.score = 0
        self.level = 1
