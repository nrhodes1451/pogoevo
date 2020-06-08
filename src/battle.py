from team import *

class Battle():
    def __init__(self, team1, team2, 
                 shields = False,
                 switching = False):
        self.teams = team1, team2
        self.victor = None
        self.shields = shields
        self.switching = switching
        self.reaction_time = 0
        self.ticker = 0


    def run_battle(self):
        # Main battle while loop
        while self.victor is None:
            

    def attack(self)