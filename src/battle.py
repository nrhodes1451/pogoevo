from team import *

class Battle():
    def __init__(self, team1, team2, 
                 shields = False,
                 switching = False):
        self.teams = team1, team2
        self.victor = None
        self.shields = shields
        self.switching = switching


    def fight(self):
        return False