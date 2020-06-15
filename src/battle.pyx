import numpy as np
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


    def run_battle(self, report = True):
        # Main battle while loop
        while self.victor is None:
            self.turn()

        if report:
            return self.generate_report()
        else:
             return True
            

    def turn(self):
        # Each turn lasts 0.5 seconds
        # Damage is dealt at the end of the move
        t1 = self.teams[0].take_turn(self.teams[1].active_poke)
        t2 = self.teams[1].take_turn(self.teams[0].active_poke)
        
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


    def generate_report(self):
        report =  {
            'team': [],
            'poke': [],
            'fast_move': [],
            'charge_move': [],
            'dmg_dealt': [],
            'dmg_taken': [],
            'turns_active': []
        }
        for i in range(len(self.teams)):
            for p in self.teams[i].pokes:
                report['team'].append(i)
                report['poke'].append(p.name)
                report['fast_move'].append(p.moveset['fast']['NAME'])
                report['charge_move'].append(p.moveset['charge']['NAME'])
                report['dmg_dealt'].append(p.damage_dealt)
                report['dmg_taken'].append(min(p.stats['sta'], 
                                               p.stats['sta'] - p.hp))
                report['turns_active'].append(p.turns_taken)


        return pd.DataFrame(report)