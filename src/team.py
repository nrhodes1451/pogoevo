from poke import *

class Team():
    def __init__(self, pokes):
        self.pokes = pokes
        self.active_poke = self.pokes[0]
        self.switching = False
        self.cooldown = 0

    
    def take_turn(self, opponent):
        if self.active_poke.hp <= 0:
            self.switch(opponent)
        elif self.switching:
            # todo
            return
        else:
            self.active_poke.attack(opponent)