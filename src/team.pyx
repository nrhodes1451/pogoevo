import numpy as np
from poke import *

class Team():
    def __init__(self, pokes):
        self.pokes = pokes
        self.active_poke = self.pokes[0]
        self.active_poke.is_active = True
        self.all_fainted = False
        self.cooldown = 0

    
    def take_turn(self, opponent):
        if np.all([p.fainted for p in self.pokes]):
            self.all_fainted = True
        elif self.active_poke.hp <= 0:
            self.switch(opponent)
        else:
            report = self.active_poke.attack(opponent)
            return report
        return None


    def switch(self, opponent):
        choices = [p for p in self.pokes
            if not (p.fainted or p.is_active)]
        self.active_poke.is_active = False
        if len(choices) == 0:
            self.all_fainted = True
            return
        elif len(choices) == 1:
            self.active_poke = choices[0]
        else:
            comparison = [p.compare(opponent) for p in choices]
            if comparison[0] > comparison[1]:
                self.active_poke = choices[0]
            else:
                self.active_poke = choices[1]
        self.active_poke.is_active = True