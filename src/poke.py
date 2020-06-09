import pandas as pd
import numpy as np
import random
import pickle as pkl
import math
from move import *

class Poke():
    def __init__(self,
                 data,
                 species,
                 ivs = [15, 15, 15],
                 level = 40,
                 moveset = None,
                 turn_length = 0.5):
        self.data = data
        self.cp_mults = data['cp']
        self.species = data['pokes'][species]
        self.type = self.get_type()
        self.ivs = ivs
        self.level = level
        self.moveset = self.get_moveset(moveset)
        self.turn_length = turn_length
        self.stats = self.calculate_stats()
        self.cp = self.calculate_cp()
        self.hp = self.stats['sta']
        self.fainted = False
        self.energy = 0
        self.cooldown = 0
        self.active_attack = None
        self.is_shadow = False


    def calculate_stats(self):
        stats = {
            'atk': self.species['atk']+self.ivs[0],
            'def': self.species['def']+self.ivs[1],
            'sta': self.species['sta']+self.ivs[2]
        }
        return stats


    def calculate_cp(self):
        return max(10, math.floor((self.stats['atk'] * 
                 self.stats['def']**0.5 *
                 self.stats['sta']**0.5 *
                 self.cp_mults[self.level]**2)/10))


    def get_moveset(self, moveset):
        if moveset is None:
            fast = self.species['field_primary_moves'].split(", ")
            charge = self.species['field_secondary_moves'].split(", ")
            return {
                'fast': Move(self.data['moves'], random.choice(fast)),
                'charge': Move(self.data['moves'], random.choice(charge))
            }
        else:
            return moveset


    def get_type(self):
        types = self.species['field_pokemon_type']
        types = types.split(", ")
        types = [t[:3] for t in types]
        return types

    
    def attack(self, opponent):
        if self.cooldown > 0:
            #todo 
            return
        elif self.charged:
            #todo
            return
        else:
            move = self.moveset['fast']
            self.active_attack = move
            self.cooldown = move.rate

        self.cooldown = self.cooldown - self.turn_length
        if self.cooldown <=0 and self.active_attack is not None:
            self.damage(move, opponent)


    def charged(self):
        return self.energy >= self.moveset['charge'].energy


    def damage(self, move, opponent):
        power = 1
        attack = 1
        modifier = 1
        defense = 1
        stab = 1 + 0.2*(move.type in self.type)
        ptype = np.prod([
            self.data['types'][move.type][t] 
            for t in opponent.type])
        weather = 1
        dodged = 1
        trainer = 1

        modifier = (ptype * 
                    stab *
                    weather * 
                    friendship * 
                    dodged * 
                    trainer * 
                    charge)
        
        damage = (0.5 *
                  power * 
                  attack * 
                  modifier /
                  defense) + 1