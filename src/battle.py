from team import *

class Battle():
    def __init__(self, team1, team2, 
                 shields = False,
                 switching = False):
        self.teams = self.order_by_attack(team1, team2)
        self.victor = None
        self.shields = shields
        self.switching = switching
        self.reaction_time = 0
        # N.B. Higher attack goes first in a move tie


    def run_battle(self):
        # Main battle while loop
        while self.victor is None:
            return
            

    def turn(self):
        # Each turn lasts 0.5 seconds
        # Damage is dealt at the end of the move
        self.teams[0].take_turn(self.teams[1].active_poke)
        self.teams[1].take_turn(self.teams[0].active_poke)


    def order_by_attack(self, t1, t2):
        if t1.active_poke.stats['atk'] > t2.active_poke.stats['atk']:
            return t1, t2
        else:
            return t2, t1