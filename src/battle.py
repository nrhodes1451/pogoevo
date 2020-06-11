from team import *

class Battle():
    def __init__(self, team1, team2, 
                 shields = False,
                 switching = False):

        # todo - this shouldn't live in instructor
        # pokes to order with each attack
        self.teams = team1, team2
        self.turn_count = 0
        self.victor = None
        self.shields = shields
        self.switching = switching
        self.reaction_time = 0
        # N.B. Higher attack goes first in a move tie


    def run_battle(self):
        # Main battle while loop
        while self.victor is None:
            self.turn()
            return
            

    def turn(self):
        # Each turn lasts 0.5 seconds
        # Damage is dealt at the end of the move
        self.teams[0].take_turn(self.teams[1].active_poke)
        self.teams[1].take_turn(self.teams[0].active_poke)
        
        if self.teams[0].all_fainted:
            self.victor = self.teams[1]
        elif self.teams[1].all_fainted:
            self.victor = self.teams[0]
        self.turn_count += 1


    def order_by_attack(self):
        if (self.teams[0].active_poke.stats['atk'] >
            self.teams[1].active_poke.stats['atk']):
            return self.teams[0], self.teams[1]
        else:
            return self.teams[1], self.teams[0]


    def get_status(self):
        return # todo