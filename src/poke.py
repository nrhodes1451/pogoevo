import pandas as pd
import numpy as np
import random
import pickle as pkl
import math

cp_mults = pkl.load(open("../data/cpmults.pkl", "rb"))

class poke():
    def __init__(self, 
                 species, 
                 ivs = [15, 15, 15],
                 level = 40,
                 moveset = None):
        self.species = species
        self.ivs = ivs
        self.level = level
        self.moveset = self.get_moveset(moveset)
        self.stats = self.calculate_stats()
        self.cp = self.calculate_cp()

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
                 cp_mults[self.level]**2)/10))

    def get_moveset(self, moveset):
        if moveset is None:
            fast = self.species['field_primary_moves'].split(", ")
            charge = self.species['field_secondary_moves'].split(", ")
            return {
                'fast': random.choice(fast),
                'charge': random.choice(charge)
            }
        else:
            return moveset