class Stats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()

        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        self.pacs_left = self.settings.pac_limit
        self.score = 0