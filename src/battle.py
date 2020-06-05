class Battle():
    def __init__(self, team1, team2):
        self.teams = team1, team2
        self.over = False
        self.victor = None

    def fight(self):
        return False